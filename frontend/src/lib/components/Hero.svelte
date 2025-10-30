<script lang="ts">
	export let name = 'Eray Aydemir';
	export let title = 'AI Developer | Full Stack Developer';
	export let description =
		'Full Stack Developer and Machine Learning Engineer specializing in deep learning, NLP, and cybersecurity applications. Conducting cutting-edge research on detecting malicious functions from reverse-engineered malware samples using LLM models.';
</script>

<section
	id="home"
	class="flex min-h-screen items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800"
>
	<div class="container mx-auto px-6 py-20">
		<div class="text-center">
			<div class="mb-8 inline-block">
				<div
					class="mx-auto flex h-32 w-32 items-center justify-center rounded-full bg-gradient-to-r from-blue-500 to-indigo-600 text-5xl font-bold text-white shadow-2xl"
				>
					{name.charAt(0)}
				</div>
			</div>

			<h1 class="animate-fade-in mb-4 text-5xl font-bold text-gray-900 md:text-7xl dark:text-white">
				{name}
			</h1>

			<h2
				class="animate-fade-in-delay-1 mb-6 text-2xl text-blue-600 md:text-3xl dark:text-blue-400"
			>
				{title}
			</h2>

			<p
				class="animate-fade-in-delay-2 mx-auto mb-8 max-w-2xl text-lg text-gray-700 md:text-xl dark:text-gray-300"
			>
				{description}
			</p>

			<div class="animate-fade-in-delay-3 flex justify-center gap-4">
				<a
					href="#projects"
					class="transform rounded-lg bg-blue-600 px-8 py-3 text-white shadow-lg transition-all hover:scale-105 hover:bg-blue-700"
				>
					View Projects
				</a>
				<a
					href="#contact"
					class="transform rounded-lg border-2 border-blue-600 bg-white px-8 py-3 text-blue-600 shadow-lg transition-all hover:scale-105 hover:bg-blue-50 dark:border-blue-400 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700"
				>
					Contact Me
				</a>
			</div>
		</div>
	</div>
</section>

<section id="about" class="bg-white py-20 dark:bg-gray-900">
	<div class="container mx-auto px-6">
		<h2 class="mb-12 text-center text-4xl font-bold text-gray-900 dark:text-white">About Me</h2>

		<div class="mx-auto max-w-4xl">
			<div class="grid gap-8 md:grid-cols-2">
				<div class="space-y-4">
					<h3 class="text-2xl font-semibold text-gray-900 dark:text-white">Background</h3>
					<p class="leading-relaxed text-gray-700 dark:text-gray-300">
						Currently pursuing MSc in Information and Data Engineering at Hacettepe University (GPA:
						3.68). Working as an AI Developer at Kloudser, developing full-stack applications and ML
						solutions. Conducting graduate research at WiseLab@Hacettepe on malware detection using
						LLM models to identify malicious functions from reverse-engineered malware samples.
					</p>
					<p class="leading-relaxed text-gray-700 dark:text-gray-300">
						<strong>Research Focus:</strong> Leveraging Large Language Models for cybersecurity applications,
						specifically detecting malicious code patterns in decompiled malware binaries.
					</p>
					<p class="leading-relaxed text-gray-700 dark:text-gray-300">
						<strong>Location:</strong> Ankara, Turkey
					</p>
				</div>

				<div class="space-y-4">
					<h3 class="text-2xl font-semibold text-gray-900 dark:text-white">Technical Skills</h3>
					<div>
						<h4 class="mb-2 text-sm font-semibold text-gray-900 dark:text-white">
							Programming Languages
						</h4>
						<div class="flex flex-wrap gap-2">
							<span
								class="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800 dark:bg-blue-900 dark:text-blue-200"
								>Python</span
							>
							<span
								class="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800 dark:bg-blue-900 dark:text-blue-200"
								>JavaScript</span
							>
							<span
								class="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800 dark:bg-blue-900 dark:text-blue-200"
								>TypeScript</span
							>
							<span
								class="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800 dark:bg-blue-900 dark:text-blue-200"
								>Java</span
							>
							<span
								class="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800 dark:bg-blue-900 dark:text-blue-200"
								>Rust</span
							>
							<span
								class="rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800 dark:bg-blue-900 dark:text-blue-200"
								>C</span
							>
						</div>
					</div>
					<div>
						<h4 class="mb-2 text-sm font-semibold text-gray-900 dark:text-white">
							ML/AI Frameworks
						</h4>
						<div class="flex flex-wrap gap-2">
							<span
								class="rounded-full bg-purple-100 px-3 py-1 text-sm text-purple-800 dark:bg-purple-900 dark:text-purple-200"
								>PyTorch</span
							>
							<span
								class="rounded-full bg-purple-100 px-3 py-1 text-sm text-purple-800 dark:bg-purple-900 dark:text-purple-200"
								>Scikit-learn</span
							>
							<span
								class="rounded-full bg-purple-100 px-3 py-1 text-sm text-purple-800 dark:bg-purple-900 dark:text-purple-200"
								>XGBoost</span
							>
							<span
								class="rounded-full bg-purple-100 px-3 py-1 text-sm text-purple-800 dark:bg-purple-900 dark:text-purple-200"
								>LLM</span
							>
							<span
								class="rounded-full bg-purple-100 px-3 py-1 text-sm text-purple-800 dark:bg-purple-900 dark:text-purple-200"
								>Hugging Face</span
							>
						</div>
					</div>
					<div>
						<h4 class="mb-2 text-sm font-semibold text-gray-900 dark:text-white">
							Web Development
						</h4>
						<div class="flex flex-wrap gap-2">
							<span
								class="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200"
								>FastAPI</span
							>
							<span
								class="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200"
								>SvelteKit</span
							>
							<span
								class="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200"
								>Spring Boot</span
							>
							<span
								class="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200"
								>Node.js</span
							>
						</div>
					</div>
					<div>
						<h4 class="mb-2 text-sm font-semibold text-gray-900 dark:text-white">Tools & Cloud</h4>
						<div class="flex flex-wrap gap-2">
							<span
								class="rounded-full bg-green-100 px-3 py-1 text-sm text-green-800 dark:bg-green-900 dark:text-green-200"
								>Docker</span
							>
							<span
								class="rounded-full bg-green-100 px-3 py-1 text-sm text-green-800 dark:bg-green-900 dark:text-green-200"
								>AWS</span
							>
							<span
								class="rounded-full bg-green-100 px-3 py-1 text-sm text-green-800 dark:bg-green-900 dark:text-green-200"
								>Git</span
							>
							<span
								class="rounded-full bg-green-100 px-3 py-1 text-sm text-green-800 dark:bg-green-900 dark:text-green-200"
								>PostgreSQL</span
							>
							<span
								class="rounded-full bg-green-100 px-3 py-1 text-sm text-green-800 dark:bg-green-900 dark:text-green-200"
								>Linux</span
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	@keyframes fade-in {
		from {
			opacity: 0;
			transform: translateY(20px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	.animate-fade-in {
		animation: fade-in 0.6s ease-out;
	}

	.animate-fade-in-delay-1 {
		animation: fade-in 0.6s ease-out 0.2s both;
	}

	.animate-fade-in-delay-2 {
		animation: fade-in 0.6s ease-out 0.4s both;
	}

	.animate-fade-in-delay-3 {
		animation: fade-in 0.6s ease-out 0.6s both;
	}
</style>
