import Add from "./routes/Add.svelte";
import Quiz from "./routes/Quiz.svelte";
import Result from "./routes/Result.svelte";

export default {
  "/": Add,
  "/add": Add,
  "/quiz": Quiz,
  "/result": Result,
};
