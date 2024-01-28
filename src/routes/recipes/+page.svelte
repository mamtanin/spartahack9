<script>
    import { onMount } from 'svelte';

    let recipeContent = ''; // Variable to store the content of the first recipe
    let recipe1Content = ''; // Variable to store the content of the second recipe

    // Function to fetch and store the contents of the recipe.txt file
    const fetchRecipe = async () => {
        try {
            const response = await fetch('recipe.txt');
            recipeContent = await response.text(); // Store the content of the file
        } catch (error) {
            console.error('Error fetching recipe:', error);
        }
    };

    // Function to fetch and store the contents of the recipe1.txt file
    const fetchRecipe1 = async () => {
        try {
            const response = await fetch('recipe1.txt');
            recipe1Content = await response.text(); // Store the content of the file
        } catch (error) {
            console.error('Error fetching recipe1:', error);
        }
    };

    // Call fetchRecipe and fetchRecipe1 functions when the component mounts
    onMount(() => {
        fetchRecipe();
        fetchRecipe1();
    });
</script>

<main>
    <h1>Recipes Page</h1>
    <a href="/">Go back to App</a>
    <a href="/composting">Go back to Composting</a> <!-- Link to composting page -->
    
    <section class="recipe">
        <h2>Recipe 1</h2>
        <pre>{recipeContent}</pre> <!-- Display the content of the first recipe -->
    </section>
    
    <section class="recipe">
        <h2>Recipe 2</h2>
        <pre>{recipe1Content}</pre> <!-- Display the content of the second recipe -->
    </section>
</main>

<style>
    main {
        text-align: center;
        padding: 4em;
        background-color: #186f50; /* Spartan green */
    }

    h1 {
        color: #ffffff; /* White */
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 20px;
    }

    a {
        text-decoration: none;
        color: #007bff;
        margin-right: 20px;
        color: #ffffff; /* White */
    }

    .recipe {
        margin-top: 40px;
        border: 1px solid #ddd;
        padding: 20px;
        border-radius: 8px;
        text-align: left;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        background-color: #ffffff; /* White */
    }

    .recipe h2 {
        font-size: 1.8em;
        font-weight: 600;
        color: #333;
        margin-bottom: 10px;
    }

    .recipe pre {
        font-family: 'Courier New', Courier, monospace;
        white-space: pre-wrap;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 4px;
    }
</style>
