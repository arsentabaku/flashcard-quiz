<script lang="ts">
  let question = "";
  let correct = "";
  let wrongs = ["", "", ""];

  async function submit() {
    const response = await fetch("http://localhost:8000/flashcards", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question,
        correct_answer: correct,
        wrong_answers: wrongs,
      }),
    });

    if (response.ok) {
      alert("✅ Flashcard added!");
      question = "";
      correct = "";
      wrongs = ["", "", ""];
    } else {
      alert("❌ Failed to add flashcard.");
    }
  }
</script>

<div class="max-w-xl mx-auto p-8  rounded-3xl shadow-2xl mt-12">
  <h1 class="text-3xl font-bold mb-6 text-center text-gray-800">
    📝 Add a Flashcard
  </h1>

  <div class="space-y-4">
    <input
      bind:value={question}
      placeholder="Enter the quiz question..."
      class="w-full p-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-400"
    />

    <input
      bind:value={correct}
      placeholder="Correct answer"
      class="w-full p-3 border border-green-400 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-300"
    />

    {#each wrongs as wrong, i}
      <input
        bind:value={wrongs[i]}
        placeholder="Wrong answer"
        class="w-full p-3 border border-red-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-200"
      />
    {/each}

    <button
      on:click={submit}
      class="w-full mt-6 bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-xl font-semibold transition"
    >
      ➕ Add Flashcard
    </button>
  </div>
</div>
