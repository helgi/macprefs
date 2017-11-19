import os
from os import path
import config
from mock import patch

def test_get_macprefs_dir():
    backup_dir = config.get_macprefs_dir()
    assert backup_dir is not None

@patch("config.makedirs")
#pylint: disable=unused-argument
def test_get_macprefs_dir_works_with_environ(makedirs_mock):
    os.environ['MACPREFS_BACKUP_DIR'] = "asdf"
    backup_dir = config.get_macprefs_dir()
    del os.environ['MACPREFS_BACKUP_DIR']
    assert "asdf" in backup_dir

@patch("config.path.exists")
@patch("config.makedirs")
def test_get_macprefs_dir_creates_if_not_exists(exists_mock, makedirs_mock):
    exists_mock.return_value = False
    config.get_macprefs_dir()
    makedirs_mock.assert_called_once()


def test_get_preferences_path():
    assert config.get_preferences_path("asdf.com") == path.join(
        config.get_preferences_backup_dir(), "asdf.com.plist")