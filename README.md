# 🧠 OpenAI Agent Runner Methods – Quick Comparison

This README provides a clear, side-by-side comparison of the three primary methods for running agents using OpenAI’s Agents SDK:

- 🔁 `Runner.run()`
- 🔃 `Runner.run_sync()`
- 🔊 `Runner.run_streamed()`

---

## 📋 Overview Table

| **Feature / Function**     | 🔁 `Runner.run()`                      | 🔃 `Runner.run_sync()`                     | 🔊 `Runner.run_streamed()`                                 |
|---------------------------|----------------------------------------|--------------------------------------------|------------------------------------------------------------|
| 🕐 **Sync or Async**       | Asynchronous (`await`)                | Synchronous (no `await`)                   | Asynchronous (`await` + `async for`)                      |
| ⏳ **How it behaves**       | Runs in background (non-blocking)     | Runs immediately but blocks the program    | Streams output live while the agent thinks                |
| 🧾 **Final Result Type**   | `RunResult`                           | `RunResult`                                | `RunResultStreaming`                                      |
| 🔍 **How output comes**    | One final result                      | One final result                           | Piece-by-piece (like real-time typing)                    |
| 💬 **Best for**            | Most general tasks                    | Simple scripts or sync apps                | Real-time chat interfaces or live feedback apps           |
| ⛓️ **Usage Style**         | `await Runner.run(...)`              | `Runner.run_sync(...)`                     | `stream = await Runner.run_streamed(...)` + `async for`   |
| 🧪 **Needs asyncio?**      | ✅ Yes                                 | ❌ No                                       | ✅ Yes                                                    |

---

## 🧠 When Should You Use Each?

### 🔁 `Runner.run()`
- **Use when**: Working in an async environment (e.g., FastAPI, Streamlit async).
- **Ideal for**: Background tasks or workflows.
- **Returns**: `RunResult` with complete output.

### 🔃 `Runner.run_sync()`
- **Use when**: You’re in a normal (non-async) script.
- **Ideal for**: Quick testing or legacy applications.
- **Returns**: Same `RunResult` but blocks execution.

### 🔊 `Runner.run_streamed()`
- **Use when**: You want real-time output as the agent generates it.
- **Ideal for**: Chatbots, assistant UIs, live planning.
- **Returns**: `RunResultStreaming`, streamed via `async for`.

---

## 💡 Example Usage

```python
# Async (background run)
result = await Runner.run(agent, "Write me a poem.")
print(result.output)

# Sync (blocking)
result = Runner.run_sync(agent, "Write a story.")
print(result.output)

# Streamed (real-time)
stream = await Runner.run_streamed(agent, "Create a plan to start a business.")
async for event in stream.stream_events():
    if hasattr(event.data, "delta"):
        print(event.data.delta, end="", flush=True)
