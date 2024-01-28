<script>
	import { onMount } from 'svelte';

	let showIngredients = false;
	let images = {};

	const handleUploadButtonClick = () => {
		// Trigger file input click when the button is clicked
		const fileInput = document.getElementById('fileInput');
		fileInput.click();
	};

	const handleFileInputChange = (event) => {
		// Handle file selection here
		const files = event.target.files;
		
		// Save the image URLs in the dictionary
		for (let i = 0; i < files.length; i++) {
			const imageUrl = URL.createObjectURL(files[i]);
			images[`image${i + 1}`] = imageUrl;
		}

		// Update flag to show Ingredients
		showIngredients = true;
	};
</script>

<main>
	<h1>Welcome!</h1>
	<div class="button-container">
		<input type="file" id="fileInput" style="display: none;" on:change={handleFileInputChange} accept="image/*" multiple>
		<button on:click={handleUploadButtonClick}>
			<img src="img.png" alt="Upload Images" style="width: 100px; height: auto;">
		</button>
		<div class="button-text">Upload Images</div>
	</div>
	{#if showIngredients}
		<div class="ingredients-container">
			<a href="/ingredients" class="ingredients-link">Ingredients</a>
		</div>
	{/if}
	<h2>
		In the United States, 80 million tons of food goes to waste every year.
		38% of all food goes uneaten*. Our aim is to utilize Artificial Intelligence to
		educate the public on how to reduce waste; thus benefiting the individual
		in terms of not wasting money on extra food. 
	</h2>
</main>

<h3>*according to <a href="https://www.feedingamerica.org/our-work/reduce-food-waste">feedingamerica.org</a></h3>

<style>
	main {
		position: relative;
		text-align: center;
		padding: 4em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #18453B;
		font-size: 6em;
		font-weight: 1000;
	}

	h2 {
		position: absolute;
		text-align: center;
		top: 120%;
		color: #000000;
		font-size: 2em;
		font-weight: 1000;
		margin-bottom: 20px;
	}

	h3 {
		position: absolute;
		bottom: 0;
		left: 50%;
		transform: translateX(-50%);
		color: #000000;
		font-size: 1em;
		font-weight: 100;
		margin-bottom: 20px;
	}

	.ingredients-container {
		margin-top: 20px;
	}

	.ingredients-link {
		color: #000000;
		font-size: 2em;
		font-weight: 1000;
		text-decoration: none;
	}

	.button-container {
		position: relative;
	}

	.button-text {
		position: absolute;
		top: 100%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	button {
		margin-top: 20px;
		border: none;
		background: none;
		cursor: pointer;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
