<script>
  import { onMount } from "svelte";

  let hash = window.location.hash;
  const params = new URLSearchParams(hash.split("?")[1]);
  let score = params.get("score") ?? "0";
  let total = 0;

  onMount(async () => {
    const res = await fetch("http://localhost:8000/quiz");
    const data = await res.json();
    total = data.length;
  });
</script>

<div
  class="max-w-lg mx-auto mt-20 p-10 bg-white rounded-3xl shadow-xl text-center text-black"
>
  <h1 class="text-3xl font-bold mb-6">🎉 Quiz Completed!</h1>

  <p class="text-xl mb-4">
    Your Score:
    <strong class="text-blue-600">{score}</strong>
    <span class="text-gray-600">/</span>
    <strong>{total}</strong>
  </p>

  <p class="text-gray-700 mb-6">
    Great job! You can play again or add new flashcards to test your knowledge.
  </p>

  <a
    href="#/quiz"
    class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl transition"
  >
    🔁 Play Again
  </a>
</div>
