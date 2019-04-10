QT += core
QT -= gui

CONFIG += c++11

TARGET = block_scan
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

INCLUDEPATH += $$PWD/include

HEADERS += \
    include/blockchain_rpc.h \
    include/common.h \
    include/db_mysql.h \
    include/init.h \
    include/json.hpp \
    include/producer.h \
    include/syncer.h \
    include/vns_rpc.h

SOURCES += \
    src/blockchain_rpc.cpp \
    src/common.cpp \
    src/db_mysql.cpp \
    src/init.cpp \
    src/main.cpp \
    src/producer.cpp \
    src/syncer.cpp \
    src/vns_rpc.cpp

unix:!macx: LIBS += -lglog
unix:!macx: LIBS += -lboost_system
unix:!macx: LIBS += -lboost_program_options
unix:!macx: LIBS += -lmysqlclient
unix:!macx: LIBS += -lpthread
unix:!macx: LIBS += -levent
unix:!macx: LIBS += -lbitcoin
unix:!macx: LIBS += -lcurl
unix:!macx: LIBS += -lrdkafka
unix:!macx: LIBS += -lrdkafka++
unix:!macx: LIBS += -lgmp

