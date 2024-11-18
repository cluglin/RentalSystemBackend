-- rental_system.house definition

CREATE TABLE `house` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '房屋id',
  `name` varchar(100) DEFAULT NULL COMMENT '房屋名稱',
  `city` varchar(50) DEFAULT NULL COMMENT '城市',
  `region` varchar(50) DEFAULT NULL COMMENT '地區',
  `address` varchar(200) DEFAULT NULL COMMENT '地址',
  `is_elevator` tinyint(1) DEFAULT '0' COMMENT '是否有電梯',
  `is_trailer` tinyint(1) DEFAULT '0' COMMENT '是否有子母車',
  `memo` varchar(100) DEFAULT NULL COMMENT '備註',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_user` int NOT NULL DEFAULT '0',
  `update_time` datetime DEFAULT NULL,
  `update_user` int DEFAULT NULL,
  `is_cancel` tinyint NOT NULL DEFAULT '0' COMMENT '軟刪',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- rental_system.function_list definition

CREATE TABLE `function_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `key` varchar(100) NOT NULL,
  `label` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='功能清單';