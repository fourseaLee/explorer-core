#include <iostream>
#include <string>
#include <fstream>
#include "common.h"
#include <glog/logging.h>
#include <curl/curl.h>
#include <gmpxx.h>

std::unique_ptr<ConfManager>confptr(new ConfManager);
ProducerKafka* g_kafka_producer = new ProducerKafka;
std::map<std::string,int> g_map_coin_coinid;
std::map<int,std::string> g_map_coinid_coin;
std::vector<std::string> g_btcminerfee_txid;
bool g_run_syncer = true;


bool ConfManager::isArgSet(const std::string& strArg)
{
    return mapArgs_.count(strArg);
}

std::string ConfManager::getArgs(const std::string& strArg,const std::string& strDefault)
{
    if(mapArgs_.count(strArg))
    {
        return mapArgs_[strArg];
    }
    return strDefault;
}

void ConfManager::readConfigFile()
{
    std::ifstream jfile(path_);

    if (!jfile)
    {
        LOG(ERROR) << "No such config file!";
        return ;
    }

    jfile >> conf_;
    if(!conf_.is_object())
    {
        conf_.clear();
        return ;
    }
    readConfJsonObj(conf_);
    conf_.clear();
}

void ConfManager::readConfJsonObj(const json js)
{
    try
    {
        auto it = js.begin();
        auto end = js.end();
        for (it; it !=end; ++it)
        {
            std::string key = it.key();
            auto val = it.value();
            if(val.is_object())
            {
                readConfJsonObj(val);
            }
            else if(val.is_string())
            {
                mapArgs_[it.key()] = val;
            }
        }
    }
    catch(...)
    {
        printArg();
        conf_.clear();
    }

}

void ConfManager::printArg()
{
    for(auto &it : mapArgs_)
        std::cout << it.first << "  :  " << it.second << std::endl;
}

static size_t ReplyCallback(void *ptr, size_t size, size_t nmemb, void *stream)
{
    std::string *str = (std::string*)stream;
    (*str).append((char*)ptr, size*nmemb);
    return size * nmemb;
}

bool CurlPost(const std::string& url,  const std::string& data,const std::string& auth, std::string& response)
{
    CURL *curl = curl_easy_init();
    struct curl_slist *headers = NULL;
    CURLcode res;
    response.clear();
    std::string error_str ;
    if (curl)
    {
        headers = curl_slist_append(headers, "content-type:application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, (long)data.size());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data.c_str());

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, ReplyCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&response);

        curl_easy_setopt(curl, CURLOPT_USERPWD, auth.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_ANY);

        curl_easy_setopt(curl, CURLOPT_USE_SSL, CURLUSESSL_TRY);
        curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 30);
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 30);
        res = curl_easy_perform(curl);
    }
    curl_easy_cleanup(curl);

    if (res != CURLE_OK)
    {
        error_str = curl_easy_strerror(res);
        LOG(ERROR) << error_str ;
        return false;
    }

    if (response.empty() || response == "")
    {
        return false;
    }
    return true;

}

bool CurlPostParams(const CurlParams &params, std::string &response)
{
    CURL *curl = curl_easy_init();
    struct curl_slist *headers = NULL;
    CURLcode res;
    response.clear();
    std::string error_str ;
    if (curl)
    {
        headers = curl_slist_append(headers, params.content_type.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_URL, params.url.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, (long)params.data.size());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, params.data.c_str());

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, ReplyCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&response);

        curl_easy_setopt(curl, CURLOPT_USERPWD, params.auth.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_ANY);

        curl_easy_setopt(curl, CURLOPT_USE_SSL, CURLUSESSL_TRY);
        curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 30);
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 30);
        res = curl_easy_perform(curl);
    }
    curl_easy_cleanup(curl);

    if (res != CURLE_OK)
    {
        error_str = curl_easy_strerror(res);
        LOG(ERROR) <<" curl error: " <<error_str ;
        return false;
    }
    return true;
}


static std::string CutString(std::string org_str,int cut_pos, bool left)
{
    std::string ret_str;
    std::string org_str_temp = org_str;

    if (left)
    {
        ret_str = org_str_temp.substr(0,cut_pos);
    }
    else
    {
        ret_str = org_str_temp.substr(cut_pos,org_str_temp.size());
    }
    return ret_str;
}

bool BigIntToPreciseFloat(const std::string& big_int_num,int div_e_pow ,int precise,std::string& precise_float)
{   
    int big_int_size = big_int_num.size() ;
    if (big_int_size < div_e_pow)
    {
        int extern_num = div_e_pow - big_int_size;
        std::string  decimal_str = "0." ;
        for(int i = 0; i < extern_num; ++i)
        {
            decimal_str = decimal_str + "0";
        }
        
        std::string no_precise_float = decimal_str + big_int_num;
        
        if  (no_precise_float.size() < precise + 2)
        {
            precise_float = no_precise_float;
        }
        else
        {
            precise_float = CutString(no_precise_float,precise + 2,true);
        }
    }
    else
    {
        std::string left_precise = CutString(big_int_num,big_int_size - div_e_pow,true);
        std::string right_precise = CutString(big_int_num,big_int_size - div_e_pow,false);

        if (right_precise.size() > precise)
        {
            std::string right_precise_cut = CutString(right_precise,precise,true);
            precise_float = left_precise + "." + right_precise_cut;
        }
        else
        {
            precise_float = left_precise + "." + right_precise;
        }

    }

    return true;
}

std::string HexToDec(const std::string &hex)
{
    mpz_class format;
    format = hex;
    return format.get_str(10);
}

std::string DecToHex(const uint64_t height)
{
    mpz_class format;
    format = height;
    std::string res = "0x" + format.get_str(16);
    return res;
}



