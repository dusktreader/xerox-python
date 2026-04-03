default: help


## ==== Template Commands ==============================================================================================

stamp:  ## Generate a test project from the template
	@uv run copier copy --trust . ..


## ==== Git Commands ===================================================================================================

git/rebase:  ## Rebase all framework branches (fastapi, flask, typerdrive) onto main
	@for branch in fastapi flask typerdrive; do \
		git checkout $$branch && git rebase main; \
	done && git checkout main

git/push:  ## Push main and all framework branches to origin
	@git push origin main && \
	for branch in fastapi flask typerdrive; do \
		git push $$branch --force-with-lease; \
	done


## ==== Testing ========================================================================================================

qa/test:  ## Run branch smoke tests (slow -- generates and tests full projects)
	@uv run pytest -m slow -v

qa/test/fast:  ## Run branch smoke tests without the slow marker filter
	@uv run pytest -v


## ==== Helpers ========================================================================================================

clean:  ## Clean up build artifacts and other junk
	@rm -rf .venv
	@uv run pyclean . --debris

help:  ## Show help message
	@awk "$$PRINT_HELP_PREAMBLE" $(MAKEFILE_LIST)


# ..... Make configuration .............................................................................................

.ONESHELL:
SHELL:=/bin/bash
.PHONY: stamp rebase push qa/test qa/test/fast clean help


# ..... Color table for pretty printing ................................................................................

RED    := \033[31m
GREEN  := \033[32m
YELLOW := \033[33m
BLUE   := \033[34m
TEAL   := \033[36m
GRAY   := \033[90m
CLEAR  := \033[0m
ITALIC := \033[3m


# ..... Hidden auxiliary targets .......................................................................................

_confirm:  # Requires confirmation before proceeding (Do not use directly)
	@if [[ -z "$(CONFIRM)" ]]; then \
		echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]; \
	fi


# ..... Help printer ...................................................................................................

define PRINT_HELP_PREAMBLE
BEGIN {
	print "Usage: $(YELLOW)make <target>$(CLEAR)"
	print
	print "Targets:"
}
/^## =+ .+( =+)?/ {
    s = $$0
    sub(/^## =+ /, "", s)
    sub(/ =+/, "", s)
	printf("\n  %s:\n", s)
}
/^## -+ .+( -+)?/ {
    s = $$0
    sub(/^## -+ /, "", s)
    sub(/ -+/, "", s)
	printf("\n    $(TEAL)> %s$(CLEAR)\n", s)
}
/^[$$()% 0-9a-zA-Z_\/-]+(\\:[$$()% 0-9a-zA-Z_\/-]+)*:.*?##/ {
    t = $$0
    sub(/:.*/, "", t)
    h = $$0
    sub(/.?*##/, "", h)
    printf("    $(YELLOW)%-19s$(CLEAR) $(GRAY)$(ITALIC)%s$(CLEAR)\n", t, h)
}
endef
export PRINT_HELP_PREAMBLE
