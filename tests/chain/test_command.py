import pytest

from vctm.chain import Command


class SuccessCommand(Command):
    executed = False

    def execute(self, context: hash) -> bool:
        return Command.SUCCESS

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        self.executed = True


class FailureCommand(SuccessCommand):
    def execute(self, context: hash) -> bool:
        return Command.FAILURE


class ErrorCommand(SuccessCommand):
    def execute(self, context: hash) -> bool:
        raise Exception('testing')


def test_success_command():
    context: hash = {}
    success: bool = True
    error: Exception = None

    cmd = SuccessCommand()

    try:
        success = cmd.execute(context)
    except Exception as exc:
        success = Command.FAILURE
        error = exc
    finally:
        cmd.post_execute(context, success, error)

    assert success == Command.SUCCESS
    assert error is None
    assert cmd.executed == True


def test_failure_command():
    context: hash = {}
    success: bool = True
    error: Exception = None

    cmd = FailureCommand()

    try:
        success = cmd.execute(context)
    except Exception as exc:
        success = Command.FAILURE
        error = exc
    finally:
        cmd.post_execute(context, success, error)

    assert success == Command.FAILURE
    assert error is None
    assert cmd.executed == True


def test_error_command():
    context: hash = {}
    success: bool = True
    error: Exception = None

    cmd = ErrorCommand()

    try:
        success = cmd.execute(context)
    except Exception as exc:
        success = Command.FAILURE
        error = exc
    finally:
        cmd.post_execute(context, success, error)

    assert success == Command.FAILURE
    assert error is not None
    assert cmd.executed == True


if __name__ == '__main__':
    pytest.main()
