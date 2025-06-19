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
   * @param {string} answer
   */
  function selectAnswer(answer) {
    if (showFeedback) return;

    selected = answer;
    isCorrect = answer === cards[current].correct_answer;
    if (isCorrect) score++;
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
  <div
    class="max-w-2xl mx-auto p-8 text-black rounded-3xl shadow-2xl mt-12 bg-white"
  >
    <h2 class="text-2xl font-bold mb-6 text-center">
      🧠 Question {current + 1} of {cards.length}
    </h2>

    <p class="text-lg mb-6 text-center">{cards[current].question}</p>

    <div class="space-y-3">
      {#each shuffle( [cards[current].correct_answer, ...cards[current].wrong_answers] ) as answer}
        <button
          class="block w-full text-left px-5 py-3 rounded-xl border-2 transition font-medium
            {selected === answer && showFeedback && isCorrect
            ? 'bg-green-100 border-green-500'
            : ''}
            {selected === answer && showFeedback && !isCorrect
            ? 'bg-red-100 border-red-500'
            : ''}
            {selected !== answer && showFeedback
            ? 'bg-gray-100 border-gray-400 cursor-not-allowed'
            : 'bg-gray-50 border-gray-300 hover:border-blue-500'}"
          disabled={showFeedback}
          on:click={() => selectAnswer(answer)}
        >
          {answer}
        </button>
      {/each}
    </div>

    {#if showFeedback}
      <div class="mt-6 text-center">
        <p class="mb-4 text-lg font-semibold">
          {isCorrect
            ? "✅ Correct!"
            : `❌ Oops! The correct answer was: ${cards[current].correct_answer}`}
        </p>
        <button
          class="bg-green-600 hover:bg-green-700 text-white px-6 py-2 rounded-xl transition"
          on:click={next}
        >
          Next Question →
        </button>
      </div>
    {/if}
  </div>
{:else if cards.length === 0}
  <div class="text-center mt-20 text-gray-600 text-lg">
    <p>No flashcards found. Please add some first.</p>
  </div>
{/if}
