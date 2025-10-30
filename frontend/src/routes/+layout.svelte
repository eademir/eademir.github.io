<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Eray Aydemir - AI Developer | Full Stack Developer</title>
	<meta
		name="description"
		content="Portfolio of Eray Aydemir, AI Developer and Full Stack Developer specializing in deep learning, NLP, and cybersecurity. Conducting research on LLM-based malicious function detection at Hacettepe University."
	/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="author" content="Eray Aydemir" />
	<meta
		name="keywords"
		content="AI Developer, Full Stack Developer, Machine Learning, Deep Learning, NLP, LLM, PyTorch, XGBoost, Cybersecurity, Malware Detection, Reverse Engineering, Eray Aydemir"
	/>
</svelte:head>

{@render children?.()}
