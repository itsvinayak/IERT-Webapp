-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: iert
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1
 /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;

/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;

/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;

/*!40101 SET NAMES utf8 */;

/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;

/*!40103 SET TIME_ZONE='+00:00' */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aside_download_link`
--

DROP TABLE IF EXISTS `aside_download_link`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `aside_download_link` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                          `title` varchar(1000) NOT NULL,
                                                                                `file` varchar(100) NOT NULL,
                                                                                                    PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aside_download_link`
--
 LOCK TABLES `aside_download_link` WRITE;

/*!40000 ALTER TABLE `aside_download_link` DISABLE KEYS */;

/*!40000 ALTER TABLE `aside_download_link` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `aside_facultys`
--

DROP TABLE IF EXISTS `aside_facultys`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `aside_facultys` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                     `name` varchar(200) NOT NULL,
                                                                         `Designation` varchar(400) NOT NULL,
                                                                                                    `Qualification` varchar(500) NOT NULL,
                                                                                                                                 `Phone` varchar(12) NOT NULL,
                                                                                                                                                     `email` varchar(254) NOT NULL,
                                                                                                                                                                          `image` varchar(100),
                                                                                                                                                                                  `branch` varchar(100) DEFAULT NULL,
                                                                                                                                                                                                                PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aside_facultys`
--
 LOCK TABLES `aside_facultys` WRITE;

/*!40000 ALTER TABLE `aside_facultys` DISABLE KEYS */;

/*!40000 ALTER TABLE `aside_facultys` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `aside_recruitment_notice`
--

DROP TABLE IF EXISTS `aside_recruitment_notice`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `aside_recruitment_notice` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                               `notice` varchar(1000) NOT NULL,
                                                                                      PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aside_recruitment_notice`
--
 LOCK TABLES `aside_recruitment_notice` WRITE;

/*!40000 ALTER TABLE `aside_recruitment_notice` DISABLE KEYS */;

/*!40000 ALTER TABLE `aside_recruitment_notice` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `auth_group` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                 `name` varchar(150) NOT NULL,
                                                                     PRIMARY KEY (`id`), UNIQUE KEY `name` (`name`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--
 LOCK TABLES `auth_group` WRITE;

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;

/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `auth_group_permissions` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                             `group_id` int(11) NOT NULL,
                                                                                `permission_id` int(11) NOT NULL,
                                                                                                        PRIMARY KEY (`id`), UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`, `permission_id`),
                                                                                                                                       KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--
 LOCK TABLES `auth_group_permissions` WRITE;

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;

/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `auth_permission` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                      `name` varchar(255) NOT NULL,
                                                                          `content_type_id` int(11) NOT NULL,
                                                                                                    `codename` varchar(100) NOT NULL,
                                                                                                                            PRIMARY KEY (`id`), UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`, `codename`)) ENGINE=MyISAM AUTO_INCREMENT=113 DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--
 LOCK TABLES `auth_permission` WRITE;

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;


INSERT INTO `auth_permission`
VALUES (1,'Can add new_by_viewer',1,'add_new_by_viewer'),
       (2,'Can change new_by_viewer',1,'change_new_by_viewer'),
       (3,'Can delete new_by_viewer',1,'delete_new_by_viewer'),
       (4,'Can view new_by_viewer',1,'view_new_by_viewer'),
       (5,'Can add new',2,'add_new'),
       (6,'Can change new',2,'change_new'),
       (7,'Can delete new',2,'delete_new'),
       (8,'Can view new',2,'view_new'),
       (9,'Can add comment',3,'add_comment'),
       (10,'Can change comment',3,'change_comment'),
       (11,'Can delete comment',3,'delete_comment'),
       (12,'Can view comment',3,'view_comment'),
       (13,'Can add notice_board',4,'add_notice_board'),
       (14,'Can change notice_board',4,'change_notice_board'),
       (15,'Can delete notice_board',4,'delete_notice_board'),
       (16,'Can view notice_board',4,'view_notice_board'),
       (17,'Can add profile',5,'add_profile'),
       (18,'Can change profile',5,'change_profile'),
       (19,'Can delete profile',5,'delete_profile'),
       (20,'Can view profile',5,'view_profile'),
       (21,'Can add user_details',6,'add_user_details'),
       (22,'Can change user_details',6,'change_user_details'),
       (23,'Can delete user_details',6,'delete_user_details'),
       (24,'Can view user_details',6,'view_user_details'),
       (25,'Can add facultys',7,'add_facultys'),
       (26,'Can change facultys',7,'change_facultys'),
       (27,'Can delete facultys',7,'delete_facultys'),
       (28,'Can view facultys',7,'view_facultys'),
       (29,'Can add recruitment_notice',8,'add_recruitment_notice'),
       (30,'Can change recruitment_notice',8,'change_recruitment_notice'),
       (31,'Can delete recruitment_notice',8,'delete_recruitment_notice'),
       (32,'Can view recruitment_notice',8,'view_recruitment_notice'),
       (33,'Can add download_link',9,'add_download_link'),
       (34,'Can change download_link',9,'change_download_link'),
       (35,'Can delete download_link',9,'delete_download_link'),
       (36,'Can view download_link',9,'view_download_link'),
       (37,'Can add message_from_about_us',10,'add_message_from_about_us'),
       (38,'Can change message_from_about_us',10,'change_message_from_about_us'),
       (39,'Can delete message_from_about_us',10,'delete_message_from_about_us'),
       (40,'Can view message_from_about_us',10,'view_message_from_about_us'),
       (41,'Can add degree_detail',11,'add_degree_detail'),
       (42,'Can change degree_detail',11,'change_degree_detail'),
       (43,'Can delete degree_detail',11,'delete_degree_detail'),
       (44,'Can view degree_detail',11,'view_degree_detail'),
       (45,'Can add gallery_pic',12,'add_gallery_pic'),
       (46,'Can change gallery_pic',12,'change_gallery_pic'),
       (47,'Can delete gallery_pic',12,'delete_gallery_pic'),
       (48,'Can view gallery_pic',12,'view_gallery_pic'),
       (49,'Can add holiday',13,'add_holiday'),
       (50,'Can change holiday',13,'change_holiday'),
       (51,'Can delete holiday',13,'delete_holiday'),
       (52,'Can view holiday',13,'view_holiday'),
       (53,'Can add popup',14,'add_popup'),
       (54,'Can change popup',14,'change_popup'),
       (55,'Can delete popup',14,'delete_popup'),
       (56,'Can view popup',14,'view_popup'),
       (57,'Can add user dashboard module',15,'add_userdashboardmodule'),
       (58,'Can change user dashboard module',15,'change_userdashboardmodule'),
       (59,'Can delete user dashboard module',15,'delete_userdashboardmodule'),
       (60,'Can view user dashboard module',15,'view_userdashboardmodule'),
       (61,'Can add bookmark',16,'add_bookmark'),
       (62,'Can change bookmark',16,'change_bookmark'),
       (63,'Can delete bookmark',16,'delete_bookmark'),
       (64,'Can view bookmark',16,'view_bookmark'),
       (65,'Can add pinned application',17,'add_pinnedapplication'),
       (66,'Can change pinned application',17,'change_pinnedapplication'),
       (67,'Can delete pinned application',17,'delete_pinnedapplication'),
       (68,'Can view pinned application',17,'view_pinnedapplication'),
       (69,'Can add association',18,'add_association'),
       (70,'Can change association',18,'change_association'),
       (71,'Can delete association',18,'delete_association'),
       (72,'Can view association',18,'view_association'),
       (73,'Can add code',19,'add_code'),
       (74,'Can change code',19,'change_code'),
       (75,'Can delete code',19,'delete_code'),
       (76,'Can view code',19,'view_code'),
       (77,'Can add nonce',20,'add_nonce'),
       (78,'Can change nonce',20,'change_nonce'),
       (79,'Can delete nonce',20,'delete_nonce'),
       (80,'Can view nonce',20,'view_nonce'),
       (81,'Can add user social auth',21,'add_usersocialauth'),
       (82,'Can change user social auth',21,'change_usersocialauth'),
       (83,'Can delete user social auth',21,'delete_usersocialauth'),
       (84,'Can view user social auth',21,'view_usersocialauth'),
       (85,'Can add partial',22,'add_partial'),
       (86,'Can change partial',22,'change_partial'),
       (87,'Can delete partial',22,'delete_partial'),
       (88,'Can view partial',22,'view_partial'),
       (89,'Can add log entry',23,'add_logentry'),
       (90,'Can change log entry',23,'change_logentry'),
       (91,'Can delete log entry',23,'delete_logentry'),
       (92,'Can view log entry',23,'view_logentry'),
       (93,'Can add permission',24,'add_permission'),
       (94,'Can change permission',24,'change_permission'),
       (95,'Can delete permission',24,'delete_permission'),
       (96,'Can view permission',24,'view_permission'),
       (97,'Can add group',25,'add_group'),
       (98,'Can change group',25,'change_group'),
       (99,'Can delete group',25,'delete_group'),
       (100,'Can view group',25,'view_group'),
       (101,'Can add user',26,'add_user'),
       (102,'Can change user',26,'change_user'),
       (103,'Can delete user',26,'delete_user'),
       (104,'Can view user',26,'view_user'),
       (105,'Can add content type',27,'add_contenttype'),
       (106,'Can change content type',27,'change_contenttype'),
       (107,'Can delete content type',27,'delete_contenttype'),
       (108,'Can view content type',27,'view_contenttype'),
       (109,'Can add session',28,'add_session'),
       (110,'Can change session',28,'change_session'),
       (111,'Can delete session',28,'delete_session'),
       (112,'Can view session',28,'view_session');

/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `auth_user` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                `password` varchar(128) NOT NULL,
                                                                        `last_login` datetime(6) DEFAULT NULL,
                                                                                                         `is_superuser` tinyint(1) NOT NULL,
                                                                                                                                   `username` varchar(150) NOT NULL,
                                                                                                                                                           `first_name` varchar(30) NOT NULL,
                                                                                                                                                                                    `last_name` varchar(150) NOT NULL,
                                                                                                                                                                                                             `email` varchar(254) NOT NULL,
                                                                                                                                                                                                                                  `is_staff` tinyint(1) NOT NULL,
                                                                                                                                                                                                                                                        `is_active` tinyint(1) NOT NULL,
                                                                                                                                                                                                                                                                               `date_joined` datetime(6) NOT NULL,
                                                                                                                                                                                                                                                                                                         PRIMARY KEY (`id`), UNIQUE KEY `username` (`username`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--
 LOCK TABLES `auth_user` WRITE;

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `auth_user_groups` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                       `user_id` int(11) NOT NULL,
                                                                         `group_id` int(11) NOT NULL,
                                                                                            PRIMARY KEY (`id`), UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`, `group_id`),
                                                                                                                           KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--
 LOCK TABLES `auth_user_groups` WRITE;

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;

/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `auth_user_user_permissions` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                                 `user_id` int(11) NOT NULL,
                                                                                   `permission_id` int(11) NOT NULL,
                                                                                                           PRIMARY KEY (`id`), UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`, `permission_id`),
                                                                                                                                          KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--
 LOCK TABLES `auth_user_user_permissions` WRITE;

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;

/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `dashboard_userdashboardmodule`
--

DROP TABLE IF EXISTS `dashboard_userdashboardmodule`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `dashboard_userdashboardmodule` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                                    `title` varchar(255) NOT NULL,
                                                                                         `module` varchar(255) NOT NULL,
                                                                                                               `app_label` varchar(255) DEFAULT NULL,
                                                                                                                                                `user` int(10) unsigned NOT NULL,
                                                                                                                                                                        `column` int(10) unsigned NOT NULL,
                                                                                                                                                                                                  `order` int(11) NOT NULL,
                                                                                                                                                                                                                  `settings` longtext NOT NULL,
                                                                                                                                                                                                                                      `children` longtext NOT NULL,
                                                                                                                                                                                                                                                          `collapsed` tinyint(1) NOT NULL,
                                                                                                                                                                                                                                                                                 PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_userdashboardmodule`
--
 LOCK TABLES `dashboard_userdashboardmodule` WRITE;

/*!40000 ALTER TABLE `dashboard_userdashboardmodule` DISABLE KEYS */;

/*!40000 ALTER TABLE `dashboard_userdashboardmodule` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `django_admin_log` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                       `action_time` datetime(6) NOT NULL,
                                                                                 `object_id` longtext,
                                                                                 `object_repr` varchar(200) NOT NULL,
                                                                                                            `action_flag` smallint(5) unsigned NOT NULL,
                                                                                                                                               `change_message` longtext NOT NULL,
                                                                                                                                                                         `content_type_id` int(11) DEFAULT NULL,
                                                                                                                                                                                                           `user_id` int(11) NOT NULL,
                                                                                                                                                                                                                             PRIMARY KEY (`id`), KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
                                                                                                                                                                                                                                                     KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--
 LOCK TABLES `django_admin_log` WRITE;

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;

/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `django_content_type` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                          `app_label` varchar(100) NOT NULL,
                                                                                   `model` varchar(100) NOT NULL,
                                                                                                        PRIMARY KEY (`id`), UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`, `model`)) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--
 LOCK TABLES `django_content_type` WRITE;

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;


INSERT INTO `django_content_type`
VALUES (1,'iert_news','new_by_viewer'),
       (2,'iert_news','new'),
       (3,'iert_news','comment'),
       (4,'extra_links','notice_board'),
       (5,'user','profile'),
       (6,'user','user_details'),
       (7,'aside','facultys'),
       (8,'aside','recruitment_notice'),
       (9,'aside','download_link'),
       (10,'home','message_from_about_us'),
       (11,'home','degree_detail'),
       (12,'home','gallery_pic'),
       (13,'home','holiday'),
       (14,'home','popup'),
       (15,'dashboard','userdashboardmodule'),
       (16,'jet','bookmark'),
       (17,'jet','pinnedapplication'),
       (18,'social_django','association'),
       (19,'social_django','code'),
       (20,'social_django','nonce'),
       (21,'social_django','usersocialauth'),
       (22,'social_django','partial'),
       (23,'admin','logentry'),
       (24,'auth','permission'),
       (25,'auth','group'),
       (26,'auth','user'),
       (27,'contenttypes','contenttype'),
       (28,'sessions','session');

/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `django_migrations` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                        `app` varchar(255) NOT NULL,
                                                                           `name` varchar(255) NOT NULL,
                                                                                               `applied` datetime(6) NOT NULL,
                                                                                                                     PRIMARY KEY (`id`)) ENGINE=MyISAM AUTO_INCREMENT=95 DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--
 LOCK TABLES `django_migrations` WRITE;

/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;


INSERT INTO `django_migrations`
VALUES (1,'contenttypes','0001_initial','2019-08-10 19:26:32.294691'),
       (2,'auth','0001_initial','2019-08-10 19:26:32.976344'),
       (3,'admin','0001_initial','2019-08-10 19:26:34.342518'),
       (4,'admin','0002_logentry_remove_auto_add','2019-08-10 19:26:34.482758'),
       (5,'admin','0003_logentry_add_action_flag_choices','2019-08-10 19:26:34.497054'),
       (6,'aside','0001_initial','2019-08-10 19:26:34.571367'),
       (7,'aside','0002_auto_20190207_1143','2019-08-10 19:26:34.650055'),
       (8,'aside','0003_facultys_image','2019-08-10 19:26:34.801424'),
       (9,'aside','0004_recruitment_notice','2019-08-10 19:26:34.882476'),
       (10,'aside','0005_download_link','2019-08-10 19:26:34.964007'),
       (11,'aside','0006_auto_20190220_1759','2019-08-10 19:26:35.348796'),
       (12,'aside','0007_auto_20190226_0709','2019-08-10 19:26:35.357312'),
       (13,'aside','0008_facultys_branch','2019-08-10 19:26:35.440763'),
       (14,'contenttypes','0002_remove_content_type_name','2019-08-10 19:26:35.951682'),
       (15,'auth','0002_alter_permission_name_max_length','2019-08-10 19:26:36.111478'),
       (16,'auth','0003_alter_user_email_max_length','2019-08-10 19:26:36.231116'),
       (17,'auth','0004_alter_user_username_opts','2019-08-10 19:26:36.257541'),
       (18,'auth','0005_alter_user_last_login_null','2019-08-10 19:26:36.354644'),
       (19,'auth','0006_require_contenttypes_0002','2019-08-10 19:26:36.357538'),
       (20,'auth','0007_alter_validators_add_error_messages','2019-08-10 19:26:36.382839'),
       (21,'auth','0008_alter_user_username_max_length','2019-08-10 19:26:36.547427'),
       (22,'auth','0009_alter_user_last_name_max_length','2019-08-10 19:26:36.682090'),
       (23,'auth','0010_alter_group_name_max_length','2019-08-10 19:26:36.771489'),
       (24,'auth','0011_update_proxy_permissions','2019-08-10 19:26:36.805749'),
       (25,'dashboard','0001_initial','2019-08-10 19:26:36.875485'),
       (26,'extra_links','0001_initial','2019-08-10 19:26:36.943428'),
       (27,'extra_links','0002_notice_board_date','2019-08-10 19:26:37.084647'),
       (28,'extra_links','0003_notice_board_branch','2019-08-10 19:26:37.289231'),
       (29,'home','0001_initial','2019-08-10 19:26:37.359262'),
       (30,'home','0002_degree_detail','2019-08-10 19:26:37.428966'),
       (31,'home','0003_gallery_pic','2019-08-10 19:26:37.495144'),
       (32,'home','0004_degree_detail_timetable','2019-08-10 19:26:37.569285'),
       (33,'home','0005_holiday','2019-08-10 19:26:37.643439'),
       (34,'home','0006_notice','2019-08-10 19:26:37.711091'),
       (35,'home','0007_auto_20190306_0947','2019-08-10 19:26:38.117611'),
       (36,'home','0008_auto_20190331_0639','2019-08-10 19:26:39.032696'),
       (37,'home','0009_remove_degree_detail_image','2019-08-10 19:26:39.113092'),
       (38,'home','0010_auto_20190403_0446','2019-08-10 19:26:39.306960'),
       (39,'home','0011_auto_20190403_0452','2019-08-10 19:26:39.315632'),
       (40,'home','0012_auto_20190403_0453','2019-08-10 19:26:39.563283'),
       (41,'home','0013_remove_degree_detail_notice','2019-08-10 19:26:39.686647'),
       (42,'home','0014_auto_20190607_0533','2019-08-10 19:26:39.842041'),
       (43,'home','0015_popup','2019-08-10 19:26:39.910362'),
       (44,'iert_news','0001_initial','2019-08-10 19:26:39.981679'),
       (45,'iert_news','0002_news_image','2019-08-10 19:26:40.232693'),
       (46,'iert_news','0003_auto_20190211_1554','2019-08-10 19:26:40.245735'),
       (47,'iert_news','0004_auto_20190211_1631','2019-08-10 19:26:40.483400'),
       (48,'iert_news','0005_auto_20190211_1640','2019-08-10 19:26:40.522125'),
       (49,'iert_news','0006_auto_20190211_2245','2019-08-10 19:26:41.196748'),
       (50,'iert_news','0007_new_likes','2019-08-10 19:26:41.368927'),
       (51,'iert_news','0008_auto_20190225_1252','2019-08-10 19:26:41.780049'),
       (52,'iert_news','0009_auto_20190225_1522','2019-08-10 19:26:41.986403'),
       (53,'iert_news','0010_auto_20190225_1539','2019-08-10 19:26:42.602937'),
       (54,'iert_news','0011_auto_20190225_1730','2019-08-10 19:26:42.643968'),
       (55,'iert_news','0012_auto_20190226_1226','2019-08-10 19:26:42.646758'),
       (56,'iert_news','0013_auto_20190226_1227','2019-08-10 19:26:42.649410'),
       (57,'iert_news','0014_new_likes','2019-08-10 19:26:42.737003'),
       (58,'iert_news','0015_comment','2019-08-10 19:26:43.633890'),
       (59,'iert_news','0016_auto_20190302_1807','2019-08-10 19:26:43.893998'),
       (60,'iert_news','0017_auto_20190302_2058','2019-08-10 19:26:44.021207'),
       (61,'iert_news','0018_new_no_of_comment','2019-08-10 19:26:44.179230'),
       (62,'iert_news','0019_auto_20190302_2134','2019-08-10 19:26:44.399294'),
       (63,'iert_news','0020_comment_reply','2019-08-10 19:26:44.496893'),
       (64,'jet','0001_initial','2019-08-10 19:26:45.007461'),
       (65,'jet','0002_delete_userdashboardmodule','2019-08-10 19:26:45.015144'),
       (66,'sessions','0001_initial','2019-08-10 19:26:45.101433'),
       (67,'default','0001_initial','2019-08-10 19:26:46.409330'),
       (68,'social_auth','0001_initial','2019-08-10 19:26:46.412944'),
       (69,'default','0002_add_related_name','2019-08-10 19:26:46.823808'),
       (70,'social_auth','0002_add_related_name','2019-08-10 19:26:46.825451'),
       (71,'default','0003_alter_email_max_length','2019-08-10 19:26:46.890326'),
       (72,'social_auth','0003_alter_email_max_length','2019-08-10 19:26:46.893441'),
       (73,'default','0004_auto_20160423_0400','2019-08-10 19:26:46.918776'),
       (74,'social_auth','0004_auto_20160423_0400','2019-08-10 19:26:46.920693'),
       (75,'social_auth','0005_auto_20160727_2333','2019-08-10 19:26:47.066572'),
       (76,'social_django','0006_partial','2019-08-10 19:26:47.143945'),
       (77,'social_django','0007_code_timestamp','2019-08-10 19:26:47.437194'),
       (78,'social_django','0008_partial_timestamp','2019-08-10 19:26:47.649134'),
       (79,'user','0001_initial','2019-08-10 19:26:47.822962'),
       (80,'user','0002_auto_20190214_0810','2019-08-10 19:26:48.749212'),
       (81,'user','0003_auto_20190214_1013','2019-08-10 19:26:49.203676'),
       (82,'user','0004_auto_20190214_1258','2019-08-10 19:26:49.236064'),
       (83,'user','0005_auto_20190214_1342','2019-08-10 19:26:49.310281'),
       (84,'user','0006_auto_20190219_1041','2019-08-10 19:26:49.320842'),
       (85,'user','0007_auto_20190220_1647','2019-08-10 19:26:49.332398'),
       (86,'user','0008_auto_20190331_0651','2019-08-10 19:26:49.412628'),
       (87,'user','0009_auto_20190403_0826','2019-08-10 19:26:49.531605'),
       (88,'user','0010_auto_20190403_0828','2019-08-10 19:46:26.521021'),
       (89,'iert_news','0021_auto_20190810_1947','2019-08-10 19:47:56.180194'),
       (90,'social_django','0001_initial','2019-08-10 19:47:56.182957'),
       (91,'social_django','0002_add_related_name','2019-08-10 19:47:56.184095'),
       (92,'social_django','0003_alter_email_max_length','2019-08-10 19:47:56.185367'),
       (93,'social_django','0004_auto_20160423_0400','2019-08-10 19:47:56.186779'),
       (94,'social_django','0005_auto_20160727_2333','2019-08-10 19:47:56.188122');

/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL,
                                                         `session_data` longtext NOT NULL,
                                                                                 `expire_date` datetime(6) NOT NULL,
                                                                                                           PRIMARY KEY (`session_key`), KEY `django_session_expire_date_a5c62663` (`expire_date`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--
 LOCK TABLES `django_session` WRITE;

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;

/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `extra_links_notice_board`
--

DROP TABLE IF EXISTS `extra_links_notice_board`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `extra_links_notice_board` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                               `topic` varchar(300) NOT NULL,
                                                                                    `info` longtext NOT NULL,
                                                                                                    `date` datetime(6) NOT NULL,
                                                                                                                       `branch` varchar(100) NOT NULL,
                                                                                                                                             PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extra_links_notice_board`
--
 LOCK TABLES `extra_links_notice_board` WRITE;

/*!40000 ALTER TABLE `extra_links_notice_board` DISABLE KEYS */;

/*!40000 ALTER TABLE `extra_links_notice_board` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `home_degree_detail`
--

DROP TABLE IF EXISTS `home_degree_detail`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `home_degree_detail` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                         `branch` varchar(300) NOT NULL,
                                                                               `branch_imformation` longtext,
                                                                               `branch_vision` longtext,
                                                                               `branch_mission` longtext,
                                                                               `branch_lab` longtext,
                                                                               `branch_syllabus` longtext,
                                                                               PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_degree_detail`
--
 LOCK TABLES `home_degree_detail` WRITE;

/*!40000 ALTER TABLE `home_degree_detail` DISABLE KEYS */;

/*!40000 ALTER TABLE `home_degree_detail` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `home_gallery_pic`
--

DROP TABLE IF EXISTS `home_gallery_pic`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `home_gallery_pic` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                       `title` varchar(200) NOT NULL,
                                                                            `image` varchar(100) NOT NULL,
                                                                                                 PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_gallery_pic`
--
 LOCK TABLES `home_gallery_pic` WRITE;

/*!40000 ALTER TABLE `home_gallery_pic` DISABLE KEYS */;

/*!40000 ALTER TABLE `home_gallery_pic` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `home_holiday`
--

DROP TABLE IF EXISTS `home_holiday`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `home_holiday` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                   `holiday_html` longtext NOT NULL,
                                                                           PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_holiday`
--
 LOCK TABLES `home_holiday` WRITE;

/*!40000 ALTER TABLE `home_holiday` DISABLE KEYS */;

/*!40000 ALTER TABLE `home_holiday` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `home_message_from_about_us`
--

DROP TABLE IF EXISTS `home_message_from_about_us`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `home_message_from_about_us` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                                 `topic` varchar(200) NOT NULL,
                                                                                      `text` longtext NOT NULL,
                                                                                                      PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_message_from_about_us`
--
 LOCK TABLES `home_message_from_about_us` WRITE;

/*!40000 ALTER TABLE `home_message_from_about_us` DISABLE KEYS */;

/*!40000 ALTER TABLE `home_message_from_about_us` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `home_popup`
--

DROP TABLE IF EXISTS `home_popup`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `home_popup` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                 `text` varchar(500) NOT NULL,
                                                                     PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_popup`
--
 LOCK TABLES `home_popup` WRITE;

/*!40000 ALTER TABLE `home_popup` DISABLE KEYS */;

/*!40000 ALTER TABLE `home_popup` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `iert_news_comment`
--

DROP TABLE IF EXISTS `iert_news_comment`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `iert_news_comment` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                        `content` varchar(300) NOT NULL,
                                                                               `time` datetime(6) DEFAULT NULL,
                                                                                                          `news_id` int(11) NOT NULL,
                                                                                                                            `user_id` int(11) NOT NULL,
                                                                                                                                              `reply_id` int(11) DEFAULT NULL,
                                                                                                                                                                         PRIMARY KEY (`id`), KEY `iert_news_comment_news_id_21072daa` (`news_id`),
                                                                                                                                                                                                 KEY `iert_news_comment_user_id_ba2219cb` (`user_id`),
                                                                                                                                                                                                     KEY `iert_news_comment_reply_id_abfcc297` (`reply_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iert_news_comment`
--
 LOCK TABLES `iert_news_comment` WRITE;

/*!40000 ALTER TABLE `iert_news_comment` DISABLE KEYS */;

/*!40000 ALTER TABLE `iert_news_comment` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `iert_news_new`
--

DROP TABLE IF EXISTS `iert_news_new`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `iert_news_new` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                    `title` varchar(300) NOT NULL,
                                                                         `author` varchar(300) NOT NULL,
                                                                                               `date` date DEFAULT NULL,
                                                                                                                   `info` longtext NOT NULL,
                                                                                                                                   `image` varchar(100) DEFAULT NULL,
                                                                                                                                                                `no_of_comment` int(11) NOT NULL,
                                                                                                                                                                                        PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iert_news_new`
--
 LOCK TABLES `iert_news_new` WRITE;

/*!40000 ALTER TABLE `iert_news_new` DISABLE KEYS */;

/*!40000 ALTER TABLE `iert_news_new` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `iert_news_new_by_viewer`
--

DROP TABLE IF EXISTS `iert_news_new_by_viewer`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `iert_news_new_by_viewer` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                              `title` varchar(300) NOT NULL,
                                                                                   `author` varchar(300) NOT NULL,
                                                                                                         `date` date DEFAULT NULL,
                                                                                                                             `image` varchar(100) DEFAULT NULL,
                                                                                                                                                          `info` longtext NOT NULL,
                                                                                                                                                                          PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iert_news_new_by_viewer`
--
 LOCK TABLES `iert_news_new_by_viewer` WRITE;

/*!40000 ALTER TABLE `iert_news_new_by_viewer` DISABLE KEYS */;

/*!40000 ALTER TABLE `iert_news_new_by_viewer` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `iert_news_new_likes`
--

DROP TABLE IF EXISTS `iert_news_new_likes`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `iert_news_new_likes` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                          `new_id` int(11) NOT NULL,
                                                                           `user_id` int(11) NOT NULL,
                                                                                             PRIMARY KEY (`id`), UNIQUE KEY `iert_news_new_likes_new_id_user_id_26078268_uniq` (`new_id`, `user_id`),
                                                                                                                            KEY `iert_news_new_likes_new_id_d460d9dc` (`new_id`),
                                                                                                                                KEY `iert_news_new_likes_user_id_8ca32d62` (`user_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iert_news_new_likes`
--
 LOCK TABLES `iert_news_new_likes` WRITE;

/*!40000 ALTER TABLE `iert_news_new_likes` DISABLE KEYS */;

/*!40000 ALTER TABLE `iert_news_new_likes` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `jet_bookmark`
--

DROP TABLE IF EXISTS `jet_bookmark`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `jet_bookmark` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                   `url` varchar(200) NOT NULL,
                                                                      `title` varchar(255) NOT NULL,
                                                                                           `user` int(10) unsigned NOT NULL,
                                                                                                                   `date_add` datetime(6) NOT NULL,
                                                                                                                                          PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jet_bookmark`
--
 LOCK TABLES `jet_bookmark` WRITE;

/*!40000 ALTER TABLE `jet_bookmark` DISABLE KEYS */;

/*!40000 ALTER TABLE `jet_bookmark` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `jet_pinnedapplication`
--

DROP TABLE IF EXISTS `jet_pinnedapplication`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `jet_pinnedapplication` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                            `app_label` varchar(255) NOT NULL,
                                                                                     `user` int(10) unsigned NOT NULL,
                                                                                                             `date_add` datetime(6) NOT NULL,
                                                                                                                                    PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jet_pinnedapplication`
--
 LOCK TABLES `jet_pinnedapplication` WRITE;

/*!40000 ALTER TABLE `jet_pinnedapplication` DISABLE KEYS */;

/*!40000 ALTER TABLE `jet_pinnedapplication` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `social_auth_association` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                              `server_url` varchar(255) NOT NULL,
                                                                                        `handle` varchar(255) NOT NULL,
                                                                                                              `secret` varchar(255) NOT NULL,
                                                                                                                                    `issued` int(11) NOT NULL,
                                                                                                                                                     `lifetime` int(11) NOT NULL,
                                                                                                                                                                        `assoc_type` varchar(64) NOT NULL,
                                                                                                                                                                                                 PRIMARY KEY (`id`), UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`, `handle`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--
 LOCK TABLES `social_auth_association` WRITE;

/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;

/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `social_auth_code` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                       `email` varchar(254) NOT NULL,
                                                                            `code` varchar(32) NOT NULL,
                                                                                               `verified` tinyint(1) NOT NULL,
                                                                                                                     `timestamp` datetime(6) NOT NULL,
                                                                                                                                             PRIMARY KEY (`id`), UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`, `code`),
                                                                                                                                                                            KEY `social_auth_code_code_a2393167` (`code`),
                                                                                                                                                                                KEY `social_auth_code_timestamp_176b341f` (`timestamp`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--
 LOCK TABLES `social_auth_code` WRITE;

/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;

/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `social_auth_nonce` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                        `server_url` varchar(255) NOT NULL,
                                                                                  `timestamp` int(11) NOT NULL,
                                                                                                      `salt` varchar(65) NOT NULL,
                                                                                                                         PRIMARY KEY (`id`), UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`, `timestamp`, `salt`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--
 LOCK TABLES `social_auth_nonce` WRITE;

/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;

/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `social_auth_partial`
--

DROP TABLE IF EXISTS `social_auth_partial`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `social_auth_partial` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                          `token` varchar(32) NOT NULL,
                                                                              `next_step` smallint(5) unsigned NOT NULL,
                                                                                                               `backend` varchar(32) NOT NULL,
                                                                                                                                     `data` longtext NOT NULL,
                                                                                                                                                     `timestamp` datetime(6) NOT NULL,
                                                                                                                                                                             PRIMARY KEY (`id`), KEY `social_auth_partial_token_3017fea3` (`token`),
                                                                                                                                                                                                     KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_partial`
--
 LOCK TABLES `social_auth_partial` WRITE;

/*!40000 ALTER TABLE `social_auth_partial` DISABLE KEYS */;

/*!40000 ALTER TABLE `social_auth_partial` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `social_auth_usersocialauth` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                                 `provider` varchar(32) NOT NULL,
                                                                                        `uid` varchar(255) NOT NULL,
                                                                                                           `extra_data` longtext NOT NULL,
                                                                                                                                 `user_id` int(11) NOT NULL,
                                                                                                                                                   PRIMARY KEY (`id`), UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`, `uid`),
                                                                                                                                                                                  KEY `social_auth_usersocialauth_user_id_17d28448` (`user_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--
 LOCK TABLES `social_auth_usersocialauth` WRITE;

/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;

/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `user_profile` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                   `image` varchar(100) NOT NULL,
                                                                        `user_id` int(11) NOT NULL,
                                                                                          PRIMARY KEY (`id`), UNIQUE KEY `user_id` (`user_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--
 LOCK TABLES `user_profile` WRITE;

/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;

/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `user_user_details`
--

DROP TABLE IF EXISTS `user_user_details`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!40101 SET character_set_client = utf8 */;


CREATE TABLE `user_user_details` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                                        `phone_no` varchar(20) NOT NULL,
                                                                               `roll_no` varchar(30) NOT NULL,
                                                                                                     `date_of_birth` date DEFAULT NULL,
                                                                                                                                  `user_id` int(11) NOT NULL,
                                                                                                                                                    `branch` varchar(200) NOT NULL,
                                                                                                                                                                          `year` varchar(20) NOT NULL,
                                                                                                                                                                                             PRIMARY KEY (`id`), UNIQUE KEY `user_id` (`user_id`)) ENGINE=MyISAM DEFAULT
CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_details`
--
 LOCK TABLES `user_user_details` WRITE;

/*!40000 ALTER TABLE `user_user_details` DISABLE KEYS */;

/*!40000 ALTER TABLE `user_user_details` ENABLE KEYS */;

UNLOCK TABLES;

--
-- Dumping routines for database 'iert'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;

/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-11  1:37:23
