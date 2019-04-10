-- --------------------------------------------------------
-- 主机:                           47.99.94.18
-- 服务器版本:                        5.7.23-0ubuntu0.16.04.1 - (Ubuntu)
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出数据库表结构
CREATE TABLE IF NOT EXISTS `asset_desc` (
        `id` int(11) NOT NULL COMMENT '主键,唯一标识',
        `name` varchar(30) DEFAULT NULL COMMENT 'kafka topic 名字 （币种的缩写名）',
        `kafka_url` varchar(200) DEFAULT NULL COMMENT 'kafka 地址',
        `node_url` varchar(200) DEFAULT NULL COMMENT 'rpc 节点调用地址',
        `wallet_url` varchar(200) DEFAULT NULL COMMENT 'wallet 调用地址',
        `auth` varchar(200) DEFAULT NULL COMMENT 'rpc 调用认证',
        `height` bigint(20) DEFAULT NULL COMMENT '块高度',
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
