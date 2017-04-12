from .constants import version
from .fixtures import elasticsearch


def test_process_is_pid_1(elasticsearch):
    assert elasticsearch.process.pid == 1


def test_process_is_running_as_the_correct_user(elasticsearch):
    assert elasticsearch.process.user == 'elasticsearch'


def test_process_is_running_the_correct_version(elasticsearch):
    print(elasticsearch.get_node_info())
    assert elasticsearch.get_node_info()['version']['number'] == version