<script>
  import { onMount } from "svelte";

  /**
   * @type {string | any[]}
   */
  let cards = [];
  let current = 0;
  let score = 0;

  let selected = "";
  let showFeedback = false;
  /**
   * @type {boolean | null}
   */
  let isCorrect = null;

  onMount(async () => {
    const res = await fetch("http://localhost:8000/quiz");
    cards = await res.json();
  });

  /**
   * @param {any[]} arr
   */
  function shuffle(arr) {
    return arr
      .map((value) => ({ value, sort: Math.random() }))
      .sort((a, b) => a.sort - b.sort)
      .map(({ value }) => value);
  }

  /**
   * @param {any} answer
   */
  function selectAnswer(answer) {
    if (showFeedback) {
      return;
    }

    selected = answer;
    isCorrect = answer === cards[current].correct_answer;

    if (isCorrect) {
      score++;
    }

    showFeedback = true;
  }

  function next() {
    selected = "";
    showFeedback = false;
    isCorrect = null;
    current++;

    if (current >= cards.length) {
      window.location.href = `#/result?score=${score}`;
    }
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
        class="block w-full text-left px-4 py-2 my-1 rounded border transition
					{selected === answer && showFeedback && isCorrect
          ? 'bg-green-200 border-green-500'
          : ''}
					{selected === answer && showFeedback && !isCorrect
          ? 'bg-red-200 border-red-500'
          : ''}
					{selected !== answer && showFeedback
          ? 'opacity-50 cursor-not-allowed'
          : 'bg-white hover:bg-blue-50'}"
        disabled={showFeedback}
        on:click={() => selectAnswer(answer)}
      >
        {answer}
      </button>
    {/each}

    {#if showFeedback}
      <div class="mt-4">
        <p class="mb-2 font-semibold">
          {isCorrect
            ? "✅ Correct!"
            : `❌ Wrong. Correct answer: ${cards[current].correct_answer}`}
        </p>
        <button
          class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded"
          on:click={next}
        >
          Next
        </button>
      </div>
    {/if}
  </div>
{:else if cards.length === 0}
  <div class="text-center mt-20">
    <p>No flashcards found. Please add some first.</p>
  </div>
{/if}
