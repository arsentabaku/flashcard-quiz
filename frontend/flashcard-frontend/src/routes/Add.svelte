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
      alert("Congrats! Flashcard added :)");
      question = "";
      correct = "";
      wrongs = ["", "", ""];
    } else {
      alert("Faced an error while adding flashcard :(");
    }
  }
</script>

<div class="max-w-md mx-auto p-6 bg-white rounded shadow mt-10">
  <h1 class="text-2xl font-bold mb-4">Add a Flashcard</h1>

  <input
    bind:value={question}
    placeholder="Question"
    class="w-full p-2 border mb-2 rounded"
  />

  <input
    bind:value={correct}
    placeholder="Correct Answer"
    class="w-full p-2 border mb-2 rounded"
  />

  {#each wrongs as wrong, i}
    <input
      bind:value={wrongs[i]}
      placeholder="Wrong Answer"
      class="w-full p-2 border mb-2 rounded"
    />
  {/each}

  <button
    on:click={submit}
    class="mt-4 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
  >
    Add Card
  </button>
</div>
