-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema prueba_1
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `prueba_1` ;

-- -----------------------------------------------------
-- Schema prueba_1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `prueba_1` DEFAULT CHARACTER SET utf8 ;
USE `prueba_1` ;

-- -----------------------------------------------------
-- Table `prueba_1`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prueba_1`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(255) NULL,
  `contrasena` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `prueba_1`.`programas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prueba_1`.`programas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `canal` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `descripcion` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_programas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_programas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `prueba_1`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
