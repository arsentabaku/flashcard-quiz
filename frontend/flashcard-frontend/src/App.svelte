<script>
  import Router  from "svelte-spa-router";
  import routes from "./routes";
</script>

<nav class="p-4 bg-gray-100 space-x-4 text-center">
  <a href="#/add" class="text-blue-600 underline">Add Flashcard</a>
  <a href="#/quiz" class="text-blue-600 underline">Play Quiz</a>
</nav>

<Router {routes} />
