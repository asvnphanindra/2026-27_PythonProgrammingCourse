# Commit message structure

For **every lab task**, make at least **four commits**. Checkpoints are about *what you finished*, not a line-count of “50% of the file.”

## Message pattern

```text
Unit-1/Task-N: <stage> — <what changed>
```

## Four required stages

| # | Stage | When to commit | Example |
|---|--------|----------------|---------|
| 1 | `scaffold` | File created + initial comments / docstring only | `Unit-1/Task-1: scaffold — create file with problem statement comments` |
| 2 | `work in progress` | Inputs and variables in place; calculation or output still missing | `Unit-1/Task-1: work in progress — read two numbers from the user` |
| 3 | `complete` | Program runs end-to-end | `Unit-1/Task-1: complete — print the sum of two numbers` |
| 4 | `fix` | After running it: typos, type conversion, formula, or output wording | `Unit-1/Task-1: fix — convert inputs to int before adding` |

If testing found no bugs, the fourth commit is still required. Make a small comment or output cleanup, or use:

```text
Unit-1/Task-N: fix — verified output with sample inputs
```

(and include any comment you add while verifying).

## Recommended approach

- Treat **work in progress** as “input and setup done,” not half the lines. These programs are short; counting 50% of lines is arbitrary.
- One task per commit; do not mix Task-1 and Task-2 in the same commit.
- Commit locally after each stage, then `git push` so the dashboard can see your history (it shows the latest commit message).
- Do not squash or rewrite history after pushing; faculty use the four commits as evidence of incremental work.
- If you add a README, use a separate commit: `docs: add student README metadata`.

## Do / don’t

**Do**

- Always include `Unit-1/Task-N` and the stage word (`scaffold`, `work in progress`, `complete`, or `fix`).
- Describe what changed in a short phrase after the dash.

**Don’t**

- Use vague messages like `update`, `final`, or `asdf`.
- Combine multiple tasks in one commit.
- Squash the four stage commits after they have been pushed.
