import pytest

from vctm.chain import Command, Chain


class SuccessCommand(Command):
    def __init__(self, name):
        self.name = name

    def execute(self, context: hash) -> bool:
        # print(f'execute() {self.name}')
        if 'count' in context:
            context['count'] += 1
        else:
            context['count'] = 1
        return Command.SUCCESS

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        # print(f'post_execute() {self.name}')
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


def test_success_chain():
    context = {}
    success = True
    error = None

    cmd0 = SuccessCommand('00')
    cmd1 = SuccessCommand('01')
    cmd2 = SuccessCommand('02')
    chain = Chain()
    chain.add(cmd0)
    chain.add(cmd1)
    chain.add(cmd2)

    try:
        success = chain.execute(context)
    except Exception as exc:
        success = Command.FAILURE
        error = exc
    finally:
        chain.post_execute(context, success, error)

    assert success == Command.SUCCESS
    assert error is None

    assert context['count'] == 3
    assert context['post_count'] == 3


def test_failure_chain():
    context = {}
    success = True
    error = None

    cmd0 = SuccessCommand('00')
    cmd1 = SuccessCommand('01')
    cmd2 = SuccessCommand('02')
    cmd3 = FailureCommand('03')
    cmd4 = SuccessCommand('04')
    chain = Chain()
    chain.add(cmd0)
    chain.add(cmd1)
    chain.add(cmd2)
    chain.add(cmd3)
    chain.add(cmd4)

    try:
        success = chain.execute(context)
    except Exception as exc:
        success = Command.FAILURE
        error = exc
    finally:
        chain.post_execute(context, success, error)

    assert success == Command.FAILURE
    assert error is None

    assert context['count'] == 4
    assert context['post_count'] == 5


def test_error_chain():
    context = {}
    success = True
    error = None

    cmd0 = SuccessCommand('00')
    cmd1 = SuccessCommand('01')
    cmd2 = SuccessCommand('02')
    cmd3 = ErrorCommand('03')
    cmd4 = SuccessCommand('04')
    chain = Chain()
    chain.add(cmd0)
    chain.add(cmd1)
    chain.add(cmd2)
    chain.add(cmd3)
    chain.add(cmd4)

    try:
        success = chain.execute(context)
    except Exception as exc:
        success = Command.FAILURE
        error = exc
    finally:
        chain.post_execute(context, success, error)

    assert success == Command.FAILURE
    assert error is not None

    assert context['count'] == 4
    assert context['post_count'] == 5


if __name__ == '__main__':
    pytest.main()
