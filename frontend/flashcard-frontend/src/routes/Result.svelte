<script>
  let hash = window.location.hash;
  let score = new URLSearchParams(hash.split("?")[1])?.get("score") ?? "0";
</script>

<div class="max-w-md mx-auto text-center p-10 bg-white rounded shadow mt-10">
  <h1 class="text-2xl font-bold mb-4">Quiz Finished! 🎉</h1>
  <p class="text-lg">Your score: <strong>{score}</strong> / 10</p>
  <a
    href="/Quiz"
    class="mt-6 inline-block bg-blue-500 text-white px-4 py-2 rounded"
    >Play Again</a
  >
</div>
