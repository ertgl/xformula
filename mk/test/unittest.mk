
.PHONY: unittest.run
unittest.run:
	$(PYTHON) -m unittest discover $(PREPEND_ARGV) -s $(TEST) -p "*_unit_test.py"


.PHONY: unittest.run.verbose
unittest.run.verbose: PREPEND_ARGV=-vv
unittest.run.verbose: unittest.run
