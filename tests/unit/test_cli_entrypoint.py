from p_grafo.adapters.cli.main import main


def test_cli_entrypoint_announces_planned_pipeline(capsys) -> None:
    main()

    assert "Sprint 2" in capsys.readouterr().out
