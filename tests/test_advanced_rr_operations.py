import pytest
import logging
import runregistry

logger = logging.getLogger(__name__)
VALID_RUN_NUMBER = 362874
VALID_DATASET_NAME = "/PromptReco/Commissioning2021/DQM"


@pytest.fixture
def setup_runregistry():
    logger.info("Connecting to development runregistry")
    runregistry.setup("development")


def test_move_datasets(setup_runregistry):
    answers = runregistry.move_datasets(
        from_=runregistry.WAITING_DQM_GUI_CONSTANT,
        to_="OPEN",
        dataset_name=VALID_DATASET_NAME,
        run=VALID_RUN_NUMBER,
        workspace="global",
    )
    # TODO: Run also with a token that has permission
    assert all([answer.status_code == 401 for answer in answers])
    answers = runregistry.move_datasets(
        from_="OPEN",
        to_="SIGNOFF",
        dataset_name=VALID_DATASET_NAME,
        run=VALID_RUN_NUMBER,
        workspace="ctpps",
    )
    # Requires permission
    assert all([answer.status_code == 401 for answer in answers])


def test_make_significant_single_run(setup_runregistry):
    # Get latest run in dev runregistry and make it significant
    run = runregistry.get_runs(limit=1, filter={})[0]
    answer = runregistry.make_significant_runs(run=run["run_number"])
    # requires permission
    assert answer.status_code == 401


def test_make_significant_multi_runs(setup_runregistry):
    # Get latest run in dev runregistry and make it significant
    run = runregistry.get_runs(limit=1, filter={})[0]
    answers = runregistry.make_significant_runs(runs=[run["run_number"]])
    # requires permission
    assert all([answer.status_code == 401 for answer in answers])


def test_reset_RR_attributes_and_refresh_runs_signed_off(setup_runregistry):
    answers = runregistry.reset_RR_attributes_and_refresh_runs(runs=VALID_RUN_NUMBER)
    # Cannot refresh runs which are not open
    assert all(
        [
            answer.status_code == 500 and "Run must be in state OPEN" in answer.text
            for answer in answers
        ]
    )


def test_manually_refresh_components_statuses_for_runs_open(setup_runregistry):
    run = runregistry.get_runs(limit=1, filter={})[0]
    answers = runregistry.manually_refresh_components_statuses_for_runs(
        runs=run["run_number"]
    )
    assert all([answer.status_code == 200 for answer in answers])


def test_reset_RR_attributes_and_refresh_runs_open(setup_runregistry):
    run = runregistry.get_runs(limit=1, filter={})[0]
    answers = runregistry.reset_RR_attributes_and_refresh_runs(runs=run["run_number"])
    assert all([answer.status_code == 200 for answer in answers])


def test_manually_refresh_components_statuses_for_runs_signed_off(setup_runregistry):
    answers = runregistry.manually_refresh_components_statuses_for_runs(
        runs=VALID_RUN_NUMBER
    )
    # Cannot refresh runs which are not open
    assert all(
        [
            answer.status_code == 500 and "Run must be in state OPEN" in answer.text
            for answer in answers
        ]
    )


def test_move_runs_no_run_arg(setup_runregistry):
    with pytest.raises(ValueError):
        # Raises ValueError
        runregistry.move_runs("OPEN", "SIGNOFF")


def test_move_single_run(setup_runregistry):
    """
    Unfortunately, this function was given a dual signature, and can return
    both a single or a list of request responses.
    """
    answer = runregistry.move_runs("OPEN", "SIGNOFF", run=VALID_RUN_NUMBER)
    # Requires permission
    assert answer.status_code == 401


def test_move_multi_runs(setup_runregistry):
    """
    Unfortunately, this function was given a dual signature, and can return
    both a single or a list of request responses.
    """
    answers = runregistry.move_runs("OPEN", "SIGNOFF", runs=[VALID_RUN_NUMBER])
    # Requires permission
    assert all([answer.status_code == 401 for answer in answers])


def test_edit_rr_lumisections(setup_runregistry):
    answer = runregistry.edit_rr_lumisections(
        VALID_RUN_NUMBER, 0, 1, "castor-castor", "GOOD"
    )
    # Requires permission
    assert answer.status_code == 401
