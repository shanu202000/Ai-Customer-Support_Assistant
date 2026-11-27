# AI pipeline playground

Use [data_flow.py](./data_flow.py) to send a sample question through the project's
real AI decision pipeline and inspect the final `Decision` model.

1. Install the project and its development dependencies if needed:
   `uv sync --group dev`
2. Ensure the project-root `.env` has a valid `DATABASE_URL` and
   `ANTHROPIC_API_KEY`. The pipeline reads its knowledge base from the database;
   Gmail credentials are not needed for this playground.
3. In VS Code, select the project's `.venv` Python interpreter and open
   `data_flow.py`. Run its `# %%` cells in the Jupyter Interactive window.
4. Edit `question`, then rerun the question and output cells. The final
   `decision` variable is an `app.ai.schemas.Decision`; its JSON is printed in
   the last cell.

This calls `app.ai.decide.decide()` directly. It does not read Gmail, send an
email, or write a ticket. It does make AI service requests and read knowledge
base entries from the configured database.
