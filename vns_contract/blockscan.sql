-- --------------------------------------------------------
-- 主机:                           192.168.0.68
-- 服务器版本:                        5.7.25-0ubuntu0.18.04.2 - (Ubuntu)
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出  表 blockscan.asset_desc 结构
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

-- 正在导出表  blockscan.asset_desc 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `asset_desc` DISABLE KEYS */;
INSERT INTO `asset_desc` (`id`, `name`, `kafka_url`, `node_url`, `wallet_url`, `auth`, `height`) VALUES
	(1, 'VNS', '192.168.0.40:9092', 'http://192.168.0.40:8585/', 'http://192.168.0.40:8585/', 'dev:a', 116301);
/*!40000 ALTER TABLE `asset_desc` ENABLE KEYS */;

-- 导出  表 blockscan.kafka_offset 结构
CREATE TABLE IF NOT EXISTS `kafka_offset` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `offset` bigint(20) NOT NULL COMMENT 'kafka offset',
  `name` varchar(50) NOT NULL DEFAULT 'test' COMMENT 'topic name',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2598 DEFAULT CHARSET=latin1;

-- 正在导出表  blockscan.kafka_offset 的数据：~34 rows (大约)
/*!40000 ALTER TABLE `kafka_offset` DISABLE KEYS */;
INSERT INTO `kafka_offset` (`id`, `offset`, `name`) VALUES
	(1, 0, 'VNS'),
	(2, 0, 'VNSContract');
/*!40000 ALTER TABLE `kafka_offset` ENABLE KEYS */;

-- 导出  表 blockscan.token_desc 结构
CREATE TABLE IF NOT EXISTS `token_desc` (
  `asset_name` varchar(30) NOT NULL DEFAULT 'test' COMMENT '主资产名称',
  `standard` varchar(50) NOT NULL DEFAULT 'ERC' COMMENT '代币执行的标准',
  PRIMARY KEY (`asset_name`,`standard`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  blockscan.token_desc 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `token_desc` DISABLE KEYS */;
INSERT INTO `token_desc` (`asset_name`, `standard`) VALUES
	('VNS', 'VRC20');
/*!40000 ALTER TABLE `token_desc` ENABLE KEYS */;

-- 导出  表 blockscan.token_standard 结构
CREATE TABLE IF NOT EXISTS `token_standard` (
  `standard` varchar(50) NOT NULL DEFAULT 'ERC',
  `detail` text,
  PRIMARY KEY (`standard`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `contract_detail` (
        `name` VARCHAR(300) NULL DEFAULT NULL COMMENT '名称',
        `symbol` VARCHAR(50) NULL DEFAULT NULL COMMENT '符号',
        `contract` VARCHAR(200) NOT NULL COMMENT '合约地址',
        `total` VARCHAR(200) NULL DEFAULT NULL COMMENT '总量',
        `decimal` INT(11) NULL DEFAULT NULL COMMENT '精度',
        `standard` VARCHAR(30) NULL DEFAULT NULL COMMENT '标准',
        PRIMARY KEY (`contract`)
        )
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;

-- 正在导出表  blockscan.token_standard 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `token_standard` DISABLE KEYS */;
INSERT INTO `token_standard` (`standard`, `detail`) VALUES
	('VRC20', '{\n	"06fdde03": "name()",\n	"095ea7b3": "approve(address,uint256)",\n	"18160ddd": "totalSupply()",\n	"23b872dd": "transferFrom(address,address,uint256)",\n	"313ce567": "decimals()",\n	"42966c68": "burn(uint256)",\n	"70a08231": "balanceOf(address)",\n	"79cc6790": "burnFrom(address,uint256)",\n	"95d89b41": "symbol()",\n	"a9059cbb": "transfer(address,uint256)",\n	"cae9ca51": "approveAndCall(address,uint256,bytes)",\n	"dd62ed3e": "allowance(address,address)",\n}');
/*!40000 ALTER TABLE `token_standard` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
