<script>
    import { onMount } from 'svelte';

    let compostingContent = ''; // Variable to store the content of the composting information

    // Function to fetch and store the contents of the composting.txt file
    const fetchCompostingInfo = async () => {
        try {
            const response = await fetch('composting.txt');
            compostingContent = await response.text(); // Store the content of the file
        } catch (error) {
            console.error('Error fetching composting information:', error);
        }
    };

    // Call fetchCompostingInfo function when the component mounts
    onMount(() => {
        fetchCompostingInfo();
    });
</script>

<main>
    
    <a href="/">Go back to App</a>
    <a href="/recipes">Recipes</a>
    <h2 style="color: #ffffff;">Composting Information </h2>
    <pre>{compostingContent}</pre> <!-- Display the composting information -->
</main>

<style>
    main {
        text-align: center;
        padding: 4em;
        background-color: #186f50; /* Spartan green */
    }

    a {
        text-decoration: none;
        color: #007bff;
        margin-right: 20px;
        color: #ffffff; /* White */
    }

    h2 {
        color: #18453B; /* Dark green */
        font-size: 1.5em;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 20px;
    }

    pre {
        font-family: 'Courier New', Courier, monospace;
        white-space: pre-wrap;
        background-color: #f8f9fa; /* Light gray */
        padding: 20px;
        border-radius: 8px;
    }
</style>
