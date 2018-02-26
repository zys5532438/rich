/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50534
Source Host           : localhost:3306
Source Database       : rich

Target Server Type    : MYSQL
Target Server Version : 50534
File Encoding         : 65001

Date: 2018-02-27 00:19:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `rpt_event_record`
-- ----------------------------
DROP TABLE IF EXISTS `rpt_event_record`;
CREATE TABLE `rpt_event_record` (
  `datetime` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `last_price` double DEFAULT NULL,
  `max_price` double DEFAULT NULL,
  `min_price` double DEFAULT NULL,
  `start_price` double DEFAULT NULL,
  `yesterday_price` double DEFAULT NULL,
  `zd_amt` double DEFAULT NULL,
  `zd_rate` double DEFAULT NULL,
  `hs_rate` double DEFAULT NULL,
  `cj_qty` bigint(20) DEFAULT NULL,
  `cj_amt` double DEFAULT NULL,
  `all_amt` double DEFAULT NULL,
  `lt_amt` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rpt_event_record
-- ----------------------------
INSERT INTO `rpt_event_record` VALUES ('2018-02-26', '浦发银行', '600000', '12.73', '12.84', '12.61', '12.77', '12.72', '0.01', '0.0786', '0.1737', '48806055', '620261080', '373651983454', '357760914434');
INSERT INTO `rpt_event_record` VALUES ('2018-02-26', '浦发银行', '600000', '12.73', '12.84', '12.61', '12.77', '12.72', '0.01', '0.0786', '0.1737', '48806055', '620261080', '373651983454', '357760914434');
