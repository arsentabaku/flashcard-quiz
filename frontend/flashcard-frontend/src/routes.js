import Add from "./routes/Add.svelte";
import Quiz from "./routes/Quiz.svelte";

export default {
  "/": Add,
  "/add": Add,
  "/quiz": Quiz
};
