
CREATE DATABASE IF NOT EXISTS `sdk` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `sdk`;

CREATE TABLE `callback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `url` varchar(512) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `clien_recharge_withdraw_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `coin_id` int(11) DEFAULT NULL,
  `from_address` varchar(255) DEFAULT NULL,
  `to_address` varchar(255) DEFAULT NULL,
  `balance` double(32,6) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `client_user_coin_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuser_id` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `coin_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `on_chain_address` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `coin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coin` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `menu` (
  `menuid` int(11) NOT NULL AUTO_INCREMENT COMMENT '菜单编号',
  `menuname` varchar(500) DEFAULT NULL COMMENT '菜单名称',
  `menutype` int(11) DEFAULT NULL COMMENT '菜单类型',
  `uri` varchar(500) DEFAULT NULL COMMENT 'uri',
  `visible` int(11) DEFAULT NULL COMMENT '是否显示',
  `parentid` int(11) DEFAULT NULL COMMENT '父编号',
  `creatorid` int(11) DEFAULT NULL COMMENT '添加人',
  `adddate` date DEFAULT NULL COMMENT '添加日期',
  `icon` varchar(300) DEFAULT NULL COMMENT 'icon',
  `corder` int(11) DEFAULT NULL COMMENT '排序',
  `menulevel` int(11) DEFAULT NULL COMMENT '菜单级别',
  PRIMARY KEY (`menuid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='系统菜单表';

CREATE TABLE `push_data_onchain_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `coin_id` int(11) DEFAULT NULL,
  `txid` varchar(1024) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `token_desc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(32) DEFAULT NULL,
  `branch` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_coin_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `coin_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_sgin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `appkey` varchar(255) DEFAULT NULL,
  `secret` varchar(255) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `callback_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;







