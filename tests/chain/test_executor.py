import pytest

from vctm.chain import Command, Chain, Executor


class SuccessCommand(Command):
    def execute(self, context: hash) -> bool:
        if 'count' in context:
            context['count'] += 1
        else:
            context['count'] = 1
        return Command.SUCCESS

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        if 'post_count' in context:
            context['post_count'] += 1
        else:
            context['post_count'] = 1


class FailureCommand(SuccessCommand):
    def execute(self, context: hash) -> bool:
        super().execute(context)
        return Command.FAILURE


class ErrorCommand(SuccessCommand):
    def execute(self, context: hash) -> bool:
        super().execute(context)
        raise Exception('testing')


def test_success_executor():
    context = {}
    cmd0 = SuccessCommand()
    cmd1 = SuccessCommand()
    cmd2 = SuccessCommand()
    cmd3 = SuccessCommand()
    cmd4 = SuccessCommand()
    executor = Executor()
    executor.add(cmd0)
    executor.add(cmd1)
    executor.add(cmd2)
    executor.add(cmd3)
    executor.add(cmd4)

    assert executor.execute(context)
    assert context['count'] == 5
    assert context['post_count'] == 5


def test_failure_executor():
    context = {}
    cmd0 = SuccessCommand()
    cmd1 = SuccessCommand()
    cmd2 = SuccessCommand()
    cmd3 = FailureCommand()
    cmd4 = SuccessCommand()
    executor = Executor()
    executor.add(cmd0)
    executor.add(cmd1)
    executor.add(cmd2)
    executor.add(cmd3)
    executor.add(cmd4)

    assert executor.execute(context) == Command.FAILURE
    assert context['count'] == 4
    assert context['post_count'] == 5


def test_error_executor():
    context = {}
    cmd0 = SuccessCommand()
    cmd1 = SuccessCommand()
    cmd2 = SuccessCommand()
    cmd3 = ErrorCommand()
    cmd4 = SuccessCommand()
    executor = Executor()
    executor.add(cmd0)
    executor.add(cmd1)
    executor.add(cmd2)
    executor.add(cmd3)
    executor.add(cmd4)

    with pytest.raises(Exception):
        executor.execute(context)
    assert context['count'] == 4
    assert context['post_count'] == 5


def test_failure_big_executor():
    context = {}

    cmd00 = SuccessCommand()
    cmd01 = SuccessCommand()
    cmd02 = SuccessCommand()
    cmd03 = SuccessCommand()
    cmd04 = SuccessCommand()

    cmd10 = SuccessCommand()
    cmd11 = SuccessCommand()
    cmd12 = SuccessCommand()
    cmd13 = FailureCommand()
    cmd14 = SuccessCommand()

    cmd20 = SuccessCommand()
    cmd21 = SuccessCommand()
    cmd22 = SuccessCommand()
    cmd23 = SuccessCommand()
    cmd24 = SuccessCommand()

    chain0 = Chain()
    chain0.add(cmd00)
    chain0.add(cmd01)
    chain0.add(cmd02)
    chain0.add(cmd03)
    chain0.add(cmd04)

    chain1 = Chain()
    chain1.add(cmd10)
    chain1.add(cmd11)
    chain1.add(cmd12)
    chain1.add(cmd13)
    chain1.add(cmd14)

    chain2 = Chain()
    chain2.add(cmd20)
    chain2.add(cmd21)
    chain2.add(cmd22)
    chain2.add(cmd23)
    chain2.add(cmd24)

    executor = Executor()
    executor.add(chain0)
    executor.add(chain1)
    executor.add(chain2)

    assert executor.execute(context) == Command.FAILURE
    assert context['count'] == 9
    assert context['post_count'] == 15


def test_error_big_executor():
    context = {}

    cmd00 = SuccessCommand()
    cmd01 = SuccessCommand()
    cmd02 = SuccessCommand()
    cmd03 = SuccessCommand()
    cmd04 = SuccessCommand()

    cmd10 = SuccessCommand()
    cmd11 = SuccessCommand()
    cmd12 = SuccessCommand()
    cmd13 = ErrorCommand()
    cmd14 = SuccessCommand()

    cmd20 = SuccessCommand()
    cmd21 = SuccessCommand()
    cmd22 = SuccessCommand()
    cmd23 = SuccessCommand()
    cmd24 = SuccessCommand()

    chain0 = Chain()
    chain0.add(cmd00)
    chain0.add(cmd01)
    chain0.add(cmd02)
    chain0.add(cmd03)
    chain0.add(cmd04)

    chain1 = Chain()
    chain1.add(cmd10)
    chain1.add(cmd11)
    chain1.add(cmd12)
    chain1.add(cmd13)
    chain1.add(cmd14)

    chain2 = Chain()
    chain2.add(cmd20)
    chain2.add(cmd21)
    chain2.add(cmd22)
    chain2.add(cmd23)
    chain2.add(cmd24)

    executor = Executor()
    executor.add(chain0)
    executor.add(chain1)
    executor.add(chain2)

    with pytest.raises(Exception):
        executor.execute(context)
    assert context['count'] == 9
    assert context['post_count'] == 15


if __name__ == '__main__':
    pytest.main()
