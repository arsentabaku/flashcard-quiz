<script>
  import Router from "svelte-spa-router";
  import routes from "./routes";
</script>

<nav class="p-4 bg-gray-100 text-center">
  <ul class="flex justify-center gap-6">
    <li>
      <a
        href="#/add"
        class="text-blue-600 font-semibold hover:underline hover:text-blue-800 transition"
      >
        ➕ Add Flashcard
      </a>
    </li>
    <li>
      <a
        href="#/quiz"
        class="text-blue-600 font-semibold hover:underline hover:text-blue-800 transition"
      >
        🎮 Play Quiz
      </a>
    </li>
  </ul>
</nav>

<main class="px-4">
  <Router {routes} />
</main>
