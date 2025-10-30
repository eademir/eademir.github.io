<script lang="ts">
	import Navigation from '$lib/components/Navigation.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import Projects from '$lib/components/Projects.svelte';
	import Contact from '$lib/components/Contact.svelte';
</script>

<div class="bg-white dark:bg-gray-900">
	<Navigation />

	<main>
		<Hero
			name="Eray Aydemir"
			title="AI Developer | Full Stack Developer"
			description="Full Stack Developer and Machine Learning Engineer specializing in deep learning, NLP, and cybersecurity. Conducting cutting-edge research at WiseLab@Hacettepe on detecting malicious functions from reverse-engineered malware samples using LLM models."
		/>

		<Projects />

		<Contact />
	</main>

	<footer class="bg-gray-900 py-8 text-white">
		<div class="container mx-auto px-6 text-center">
			<p class="text-gray-400">
				© {new Date().getFullYear()} Eray Aydemir. All rights reserved.
			</p>
			<p class="mt-2 text-sm text-gray-500">Built with SvelteKit & Tailwind CSS</p>
		</div>
	</footer>
</div>
