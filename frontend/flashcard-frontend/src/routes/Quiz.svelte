<script>
  import { onMount } from "svelte";

  /**
   * @type {string | any[]}
   */
  let cards = [];
  let current = 0;
  let score = 0;
  let selected = "";

  onMount(async () => {
    const res = await fetch("http://localhost:8000/quiz");
    cards = await res.json();
  });

  function submitAnswer() {
    const card = cards[current];
    if (selected === card.correct_answer) {
      score++;
    }

    selected = "";
    current++;

    if (current >= cards.length) {
      window.location.href = "#/result?score=" + score;
    }
  }

  /**
   * @param {any[]} arr
   */
  function shuffle(arr) {
    return arr
      .map((value) => ({ value, sort: Math.random() }))
      .sort((a, b) => a.sort - b.sort)
      .map(({ value }) => value);
  }
</script>

{#if cards.length > 0 && current < cards.length}
  <div class="max-w-xl mx-auto p-6 bg-white rounded shadow mt-10">
    <h2 class="text-xl font-bold mb-4">
      Question {current + 1} of {cards.length}
    </h2>
    <p class="mb-4">{cards[current].question}</p>

    {#each shuffle( [cards[current].correct_answer, ...cards[current].wrong_answers] ) as answer}
      <button
        class="block w-full text-left px-4 py-2 my-1 rounded border
				       {selected === answer ? 'bg-blue-100' : 'bg-white'}"
        on:click={() => (selected = answer)}
      >
        {answer}
      </button>
    {/each}

    {#if selected}
      <button
        class="mt-4 bg-green-500 text-white px-4 py-2 rounded"
        on:click={submitAnswer}
      >
        Next
      </button>
    {/if}
  </div>
{/if}
