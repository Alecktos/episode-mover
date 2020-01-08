import os
import time
import unittest
import subprocess
import sys

from tests.utils import file_mover_tester


class TestWatcher(unittest.TestCase, file_mover_tester.FileMoverTester):

    auto_turn_off = 10  # Turn off after 10 seconds

    def setUp(self):
        self._create_test_dirs()

    def tearDown(self):
        self._delete_test_dirs()

    def __get_destination_path_file_1(self):
        return f'{self._SHOW_DESTINATION_DIRECTORY}/kolla/Season 4/kolla.S04E15.asswe.xTTT-RR[abf].mkv'

    def create_file(self, path):
        os.open(path, os.O_CREAT)

    def test_moving_application(self):
        process = self.__run_app()
        time.sleep(5)

        file_name = 'kolla.S04E15.asswe.xTTT-RR[abf].mkv'
        self.create_file(f'{self._SOURCE_DIRECTORY}/{file_name}')

        for line in process.stdout.readlines():
            print(line)

        file_is_in_new_path = os.path.isfile(self.__get_destination_path_file_1())

        self.assertTrue(file_is_in_new_path)

    def __run_app(self):
        args = f'{self._SOURCE_DIRECTORY} {self._SHOW_DESTINATION_DIRECTORY} {self._MOVIE_DESTINATION_DIRECTORY} -q {self.auto_turn_off}'
        execution = f'{sys.executable} -m memover watch {args}'
        p = subprocess.Popen(execution, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p
