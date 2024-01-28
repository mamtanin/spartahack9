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
    <div class="header">
        <h1 style="color: #ffffff;">WasteLess</h1>
    </div>
    <div class="upload-container">
        <div class="button-container">
            <input type="file" id="fileInput" style="display: none;" on:change={handleFileInputChange} accept="image/*" multiple>
            <button on:click={handleUploadButtonClick}>
                <img src="img.png" alt="Upload Images" style="width: 180px; height: auto;">
            </button>
            <div class="button-text">Upload Images</div>
        </div>
        {#if showIngredients}
        <div class="ingredients-container">
            <a href="/recipes" class="recipe-link">Explore Recipes</a>
            <a href="/composting" class="recipe-link">Learn About Composting</a>
        </div>
        {/if}
    </div>
    <div class="description-container">
        <p class="description">
            In the United States, 80 million tons of food goes to waste every year.
            38% of all food goes uneaten*. Our aim is to utilize Artificial Intelligence to
            educate the public on how to reduce waste; thus benefiting the individual
            in terms of not wasting money on extra food.
        </p>
        <h3>
            *according to <a href="https://www.feedingamerica.org/our-work/reduce-food-waste" style="color: #007bff;">feedingamerica.org</a>
        </h3>
    </div>
</main>

<style>

    main {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
		text-align: center;
        padding: 4em;
        background-color: #186f50; /* Spartan green */
    }

    .header {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1000;
    }

    .upload-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 30vh; /* Adjust as needed */
        margin-bottom: 20vh; /* Adjust as needed */
    }

    .button-container {
        position: relative;
        margin-bottom: 20px;
    }

    button {
        border: none;
        background: none;
        cursor: pointer;
    }

    .button-text {
        font-size: 1.2em;
        margin-top: 10px;
        color: #000000; /* Green */
    }

    .ingredients-container {
        margin-top: 10px; /* Adjust as needed */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .recipe-link {
        color: #000000; /* Purple */
        font-size: 1.2em;
        font-weight: bold;
        text-decoration: none;
        margin-bottom: 10px;
        transition: color 0.3s ease;
    }

    .recipe-link:hover {
        color: #5f009f; /* Dark Purple */
    }

    .description-container {
        margin-bottom: 20vh; /* Adjust as needed */
    }

    .description {
        font-size: 1.2em;
        line-height: 1.5;
        max-width: 800px;
        margin-bottom: 20px;
        color: #ffffff; /* Black */
    }

    h3 {
        font-size: 1em;
    }

    h3 a {
        color: #007bff; /* Blue */
        text-decoration: underline;
    }
</style>
