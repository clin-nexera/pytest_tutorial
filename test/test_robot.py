import pytest

from src.robot import FakeRobot

@pytest.fixture
def robot():
    return FakeRobot()

@pytest.fixture
def connected_robot(robot):
    robot.connect()
    yield robot
    robot.disconnect()

@pytest.fixture
def connected_robot_2(robot):
    robot.connect()
    yield
    robot.disconnect()

class TestRobot:

    def test_robot_move(self, capsys, connected_robot):
        connected_robot.move()
        output = capsys.readouterr().out
        assert "Robot is moving\n" in output
        assert "Robot moved\n" in output


    @pytest.mark.usefixtures("connected_robot_2")
    def test_robot_move_2(self, capsys, robot):
        robot.move()
        output = capsys.readouterr().out
        assert "Robot is moving\n" in output
        assert "Robot moved\n" in output