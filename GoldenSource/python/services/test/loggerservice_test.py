import unittest, os

from GoldenSource.python.common.domain import Domain
from GoldenSource.python.services.logger_service import LoggerService
from GoldenSource.python.common.config import LocalConfigurator

class TestConfigurator(LocalConfigurator):
    def parse(self, args=None, fail_on_err=False):
        args = ['--home-path', os.environ.get("PROJECT_BUILD_DIR")]
        return super(TestConfigurator, self).parse(args, fail_on_err)
    
# @unittest.skip
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.logger_service = Domain(TestConfigurator).get_service(LoggerService)
    
    @unittest.skip
    def test_log(self):
        self.logger_service.log('debug2', 'DEBUG2')
        self.logger_service.log('debug', 'DEBUG')
        self.logger_service.log('info', 'INFO')
        self.logger_service.log('info')
        self.logger_service.log('warning', 'WARNING')
        self.logger_service.log('error', 'ERROR')
        self.logger_service.log('critical', 'CRITICAL')

        try:
            raise Exception('test')
        except:
            self.logger_service.log(self.logger_service.ex2str(), "CRITICAL")

    def test_logger(self):
        logger = self.logger_service.get_logger()
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        try:
            raise Exception('test')
        except:
            logger.info(logger.ex2str())
        
    def test_named_logger(self):
        logger = self.logger_service.get_logger('my_logger')
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        try:
            raise Exception('test')
        except:
            logger.info(logger.ex2str())

    def test_log_level_change(self):
        self.logger_service.set_log_level('debug')
        logger = self.logger_service.get_logger()
        logger.critical("+----------------------------+")
        logger.critical("| Everything shoud be logged |")
        logger.critical("+----------------------------+")
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        try:
            raise Exception('test')
        except:
            logger.info(logger.ex2str())

        self.logger_service.set_log_level('WARNING')
        logger.critical("+--------------------+")
        logger.critical("| Logging >= Warning |")
        logger.critical("+--------------------+")
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        try:
            raise Exception('test')
        except:
            logger.info(logger.ex2str())
        
        self.logger_service.revert_log_level()


if __name__ == '__main__':
    unittest.main()