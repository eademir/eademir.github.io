<script lang="ts">
	type Project = {
		id: number;
		title: string;
		description: string;
		category: 'web' | 'ml';
		tags: string[];
		link?: string;
		github?: string;
		paper?: string;
		image?: string;
	};

	let projects: Project[] = [
		{
			id: 1,
			title: 'LLM-Based Malicious Function Detection',
			description:
				'Graduate research project using Large Language Models to detect malicious functions in reverse-engineered malware samples. Developing novel approaches for analyzing decompiled code patterns.',
			category: 'ml',
			tags: ['LLM', 'Reverse Engineering', 'PyTorch', 'Hugging Face', 'Cybersecurity'],
			github: 'https://github.com/eademir'
		},
		{
			id: 2,
			title: 'Personal Portfolio Website',
			description:
				'Modern, responsive portfolio website built with SvelteKit and Tailwind CSS. Features project showcase and contact form with FastAPI backend for form handling.',
			category: 'web',
			tags: ['SvelteKit', 'TypeScript', 'Tailwind CSS', 'Python', 'FastAPI'],
			link: 'https://eademir.dev',
			github: 'https://github.com/eademir/eademir.github.io'
		},
		{
			id: 3,
			title: 'Tuvens - Event Curation Platform',
			description:
				'Full-stack event curation platform enabling users to discover, create, and manage events. Built with SvelteKit frontend, NestJS backend, AWS RDS PostgreSQL database, Cognito authentication, and S3 for storage.',
			category: 'web',
			tags: ['SvelteKit', 'NestJS', 'Node.js', 'PostgreSQL', 'AWS Cognito', 'S3', 'Tailwind CSS'],
			link: 'https://tuvens.com'
		},
		{
			id: 4,
			title: 'Strand345 - Dynamic Website',
			description:
				'Dynamic website with interactive pages and integrated contact form. Built with SvelteKit, Tailwind CSS, Python backend, and Google Cloud API integration.',
			category: 'web',
			tags: ['SvelteKit', 'TypeScript', 'Tailwind CSS', 'Python', 'Google Cloud API'],
			link: 'https://strand345.com'
		},
		{
			id: 5,
			title: 'NGO Hukuk - Legal Blog',
			description:
				'Professional legal blog platform with content management system, article publishing, and SEO optimization. Built with Next.js and Tailwind CSS frontend, FastAPI backend, PostgreSQL database, deployed on VPS with Docker and Nginx.',
			category: 'web',
			tags: ['Next.js', 'Tailwind CSS', 'Python', 'FastAPI', 'PostgreSQL', 'Docker', 'Nginx'],
			link: 'https://ngohukuk.com'
		},
		{
			id: 6,
			title: 'GeoID - Business Website',
			description:
				'Professional business website with integrated contact form. Built with SvelteKit and Tailwind CSS featuring dark/light theme toggle for enhanced user experience.',
			category: 'web',
			tags: ['SvelteKit', 'Tailwind CSS', 'Dark/Light Themes', 'Forms'],
			link: 'https://geoid.com.au'
		},
		{
			id: 7,
			title: 'LLM-Powered Android UI Agent',
			description:
				'Designed Python agent integrating fine-tuned LLM with adb and emulator for autonomous UI exploration and interaction.',
			category: 'ml',
			tags: ['Python', 'LLM', 'Android', 'ADB'],
			github: 'https://github.com/eademir'
		},
		{
			id: 8,
			title: 'Android Malware Detection',
			description:
				'Built and deployed calibrated XGBoost model on 200K×44K dataset achieving 98% validation accuracy. Calibration ensures reliable probability outputs for better decision-making. Used reverse engineering and static analysis for feature extraction.',
			category: 'ml',
			tags: ['XGBoost', 'Calibration', 'Scikit-learn', 'FastAPI', 'Docker'],
			github: 'https://github.com/eademir'
		},
		{
			id: 9,
			title: 'Android Malware Type Classification',
			description:
				'Multi-class classification system using calibrated XGBoost to identify malware types including Trojan, Downloader, Dropper, and other variants. Achieved 94% accuracy with calibrated probability outputs for reliable predictions.',
			category: 'ml',
			tags: ['XGBoost', 'Calibration', 'Classification', 'Python', 'Malware Analysis'],
			github: 'https://github.com/eademir'
		},
		{
			id: 10,
			title: 'Binary Text Classification for Suicide Detection',
			description:
				'Compared LSTM with BERT embeddings and TF-IDF-based neural networks achieving ~93% accuracy for suicide risk detection.',
			category: 'ml',
			tags: ['LSTM', 'BERT', 'NLP', 'PyTorch'],
			github: 'https://github.com/eademir/suicide_detection',
			paper: 'https://github.com/eademir/suicide_detection/blob/main/article.pdf',
			link: 'https://www.kaggle.com/code/eademir/suicide-detection-using-nlp'
		},
		{
			id: 11,
			title: 'Android Permissions Analyzer',
			description:
				"Extracts Android apps' permissions and explains to users what the app is capable of using fine-tuned Mistral 8B model.",
			category: 'ml',
			tags: ['Mistral 8B', 'Fine-tuning', 'Android', 'NLP'],
			github: 'https://github.com/eademir'
		},
		{
			id: 12,
			title: 'Windows Malware Classification',
			description:
				'Implemented CNN model on executable-to-image transformations for malware research and classification.',
			category: 'ml',
			tags: ['CNN', 'Deep Learning', 'Python', 'Image Processing'],
			github: 'https://github.com/eademir'
		}
	];

	let selectedCategory: 'all' | 'web' | 'ml' = $state('all');

	let filteredProjects = $derived(
		selectedCategory === 'all' ? projects : projects.filter((p) => p.category === selectedCategory)
	);
</script>

<section id="projects" class="bg-gray-50 py-20 dark:bg-gray-800">
	<div class="container mx-auto px-6">
		<h2 class="mb-4 text-center text-4xl font-bold text-gray-900 dark:text-white">My Projects</h2>
		<p class="mx-auto mb-12 max-w-2xl text-center text-gray-600 dark:text-gray-400">
			A collection of my work in web development and machine learning
		</p>

		<!-- Filter Buttons -->
		<div class="mb-12 flex flex-wrap justify-center gap-4">
			<button
				onclick={() => (selectedCategory = 'all')}
				class="transform cursor-pointer rounded-lg px-6 py-2 transition-all hover:scale-105 {selectedCategory ===
				'all'
					? 'bg-blue-600 text-white shadow-lg'
					: 'bg-white text-gray-700 hover:bg-gray-100 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'}"
			>
				All Projects
			</button>
			<button
				onclick={() => (selectedCategory = 'web')}
				class="transform cursor-pointer rounded-lg px-6 py-2 transition-all hover:scale-105 {selectedCategory ===
				'web'
					? 'bg-blue-600 text-white shadow-lg'
					: 'bg-white text-gray-700 hover:bg-gray-100 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'}"
			>
				Web Development
			</button>
			<button
				onclick={() => (selectedCategory = 'ml')}
				class="transform cursor-pointer rounded-lg px-6 py-2 transition-all hover:scale-105 {selectedCategory ===
				'ml'
					? 'bg-blue-600 text-white shadow-lg'
					: 'bg-white text-gray-700 hover:bg-gray-100 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'}"
			>
				Machine Learning
			</button>
		</div>

		<!-- Projects Grid -->
		<div class="mx-auto grid max-w-7xl gap-8 md:grid-cols-2 lg:grid-cols-3">
			{#each filteredProjects as project (project.id)}
				<div
					class="transform overflow-hidden rounded-xl bg-white shadow-lg transition-all hover:scale-105 hover:shadow-2xl dark:bg-gray-900"
				>
					<!-- Project Image Placeholder -->
					<div
						class="h-48 bg-gradient-to-br {project.category === 'web'
							? 'from-blue-400 to-blue-600'
							: 'from-purple-400 to-purple-600'} flex items-center justify-center"
					>
						<svg
							class="h-20 w-20 text-white opacity-50"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							{#if project.category === 'web'}
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"
								></path>
							{:else}
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
								></path>
							{/if}
						</svg>
					</div>

					<div class="p-6">
						<div class="mb-3 flex items-center justify-between">
							<h3 class="text-xl font-bold text-gray-900 dark:text-white">
								{project.title}
							</h3>
							<span
								class="rounded-full px-3 py-1 text-xs {project.category === 'web'
									? 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200'
									: 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200'}"
							>
								{project.category === 'web' ? 'Web Dev' : 'ML/DL'}
							</span>
						</div>

						<p class="mb-4 text-sm leading-relaxed text-gray-600 dark:text-gray-400">
							{project.description}
						</p>

						<div class="mb-4 flex flex-wrap gap-2">
							{#each project.tags as tag}
								<span
									class="rounded bg-gray-100 px-2 py-1 text-xs text-gray-700 dark:bg-gray-800 dark:text-gray-300"
								>
									{tag}
								</span>
							{/each}
						</div>

						{#if project.category === 'web'}
							<div class="flex gap-3">
								{#if project.github}
									<a
										href={project.github}
										target="_blank"
										rel="noopener noreferrer"
										class="flex items-center gap-2 rounded-lg bg-gray-800 px-4 py-2 text-sm text-white transition-colors hover:bg-gray-900 dark:bg-gray-700 dark:hover:bg-gray-600"
									>
										<svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
											<path
												d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
											/>
										</svg>
										GitHub
									</a>
								{/if}
								{#if project.link}
									<a
										href={project.link}
										target="_blank"
										rel="noopener noreferrer"
										class="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-sm text-white transition-colors hover:bg-blue-700"
									>
										<svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
												d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
											></path>
										</svg>
										Visit Site
									</a>
								{/if}
							</div>
						{:else}
							<div class="flex flex-wrap gap-3">
								{#if project.paper}
									<a
										href={project.paper}
										target="_blank"
										rel="noopener noreferrer"
										class="flex items-center gap-2 rounded-lg bg-red-600 px-4 py-2 text-sm text-white transition-colors hover:bg-red-700"
									>
										<svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
												d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
											></path>
										</svg>
										Paper
									</a>
								{/if}
								{#if project.link}
									<a
										href={project.link}
										target="_blank"
										rel="noopener noreferrer"
										class="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-sm text-white transition-colors hover:bg-blue-700"
									>
										<svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
											<path
												d="M18.5 2c-1 0-1.5.5-2.4 1.4L11.2 8l-.8-.8c-1.2-1.2-3.2-1.2-4.4 0-1.2 1.2-1.2 3.2 0 4.4l.8.8-4.6 4.6C1.5 17.9 1 18.5 1 19.5c0 1.1.9 2 2 2h.5c1 0 1.5-.5 2.4-1.4l4.6-4.6.8.8c1.2 1.2 3.2 1.2 4.4 0 1.2-1.2 1.2-3.2 0-4.4l-.8-.8L19.6 6c1-.9 1.4-1.4 1.4-2.4 0-1.7-1.3-2.6-2.5-2.6zm-8.8 9.2L13.2 15c.1.1.1.3 0 .4-.1.1-.3.1-.4 0L9.3 11.6l.4-.4zm10.2-7.1L15.3 8.7l-.4-.4 4.6-4.6c.4-.4.7-.6 1-.6.5 0 1 .4 1 1.1 0 .3-.2.6-.6.9zM3.3 19c-.4.4-.7.6-1 .6H3c-.6 0-1-.4-1-1 0-.3.2-.6.6-1L7.2 13l.4.4-4.3 4.6zm10.4-6.8l-1.4-1.4c-.1-.1-.1-.3 0-.4.1-.1.3-.1.4 0l1.4 1.4c.1.1.1.3 0 .4-.1.1-.3.1-.4 0z"
											/>
										</svg>
										Kaggle
									</a>
								{/if}
							</div>
						{/if}
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>
