<script lang="ts">
	let formData = $state({
		name: '',
		email: '',
		subject: '',
		message: ''
	});

	let errors = $state({
		name: '',
		email: '',
		subject: '',
		message: ''
	});

	let isSubmitting = $state(false);
	let submitStatus: 'idle' | 'success' | 'error' = $state('idle');

	function validateEmail(email: string): boolean {
		const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		return re.test(email);
	}

	function validateForm(): boolean {
		let isValid = true;
		errors = { name: '', email: '', subject: '', message: '' };

		if (!formData.name.trim()) {
			errors.name = 'Name is required';
			isValid = false;
		}

		if (!formData.email.trim()) {
			errors.email = 'Email is required';
			isValid = false;
		} else if (!validateEmail(formData.email)) {
			errors.email = 'Please enter a valid email';
			isValid = false;
		}

		if (!formData.subject.trim()) {
			errors.subject = 'Subject is required';
			isValid = false;
		}

		if (!formData.message.trim()) {
			errors.message = 'Message is required';
			isValid = false;
		} else if (formData.message.trim().length < 10) {
			errors.message = 'Message must be at least 10 characters';
			isValid = false;
		}

		return isValid;
	}

	async function handleSubmit(e: Event) {
		e.preventDefault();

		if (!validateForm()) {
			return;
		}

		isSubmitting = true;
		submitStatus = 'idle';

		try {
			const response = await fetch('http://localhost:8000/contact', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(formData)
			});

			if (!response.ok) {
				throw new Error('Failed to send message');
			}

			submitStatus = 'success';
			formData = { name: '', email: '', subject: '', message: '' };

			// Reset success message after 5 seconds
			setTimeout(() => {
				submitStatus = 'idle';
			}, 5000);
		} catch (error) {
			console.error('Error submitting form:', error);
			submitStatus = 'error';
		} finally {
			isSubmitting = false;
		}
	}
</script>

<section id="contact" class="bg-white py-20 dark:bg-gray-900">
	<div class="container mx-auto px-6">
		<div class="mx-auto max-w-4xl">
			<h2 class="mb-4 text-center text-4xl font-bold text-gray-900 dark:text-white">
				Get In Touch
			</h2>
			<p class="mb-12 text-center text-gray-600 dark:text-gray-400">
				Have a project in mind or just want to chat? Feel free to reach out!
			</p>

			<!-- Contact Info -->
			<div class="mx-auto max-w-3xl">
				<div class="grid gap-6 md:grid-cols-2">
					<!-- Email -->
					<a
						href="mailto:me@eademir.dev"
						class="flex cursor-pointer items-center gap-4 rounded-xl bg-white p-6 shadow-lg transition-all hover:scale-105 hover:shadow-xl dark:bg-gray-800"
					>
						<div
							class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-lg bg-blue-100 dark:bg-blue-900"
						>
							<svg
								class="h-7 w-7 text-blue-600 dark:text-blue-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
								></path>
							</svg>
						</div>
						<div>
							<h4 class="mb-1 font-semibold text-gray-900 dark:text-white">Email</h4>
							<p class="text-sm text-gray-600 dark:text-gray-400">me@eademir.dev</p>
						</div>
					</a>

					<!-- GitHub -->
					<a
						href="https://github.com/eademir"
						target="_blank"
						rel="noopener noreferrer"
						class="flex cursor-pointer items-center gap-4 rounded-xl bg-white p-6 shadow-lg transition-all hover:scale-105 hover:shadow-xl dark:bg-gray-800"
					>
						<div
							class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-lg bg-blue-100 dark:bg-blue-900"
						>
							<svg
								class="h-7 w-7 text-blue-600 dark:text-blue-400"
								fill="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
								/>
							</svg>
						</div>
						<div>
							<h4 class="mb-1 font-semibold text-gray-900 dark:text-white">GitHub</h4>
							<p class="text-sm text-gray-600 dark:text-gray-400">github.com/eademir</p>
						</div>
					</a>

					<!-- LinkedIn -->
					<a
						href="https://www.linkedin.com/in/eray-aydemir/"
						target="_blank"
						rel="noopener noreferrer"
						class="flex cursor-pointer items-center gap-4 rounded-xl bg-white p-6 shadow-lg transition-all hover:scale-105 hover:shadow-xl dark:bg-gray-800"
					>
						<div
							class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-lg bg-blue-100 dark:bg-blue-900"
						>
							<svg
								class="h-7 w-7 text-blue-600 dark:text-blue-400"
								fill="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
								/>
							</svg>
						</div>
						<div>
							<h4 class="mb-1 font-semibold text-gray-900 dark:text-white">LinkedIn</h4>
							<p class="text-sm text-gray-600 dark:text-gray-400">linkedin.com/in/eray-aydemir</p>
						</div>
					</a>

					<!-- Kaggle -->
					<a
						href="https://www.kaggle.com/erayaydemir"
						target="_blank"
						rel="noopener noreferrer"
						class="flex cursor-pointer items-center gap-4 rounded-xl bg-white p-6 shadow-lg transition-all hover:scale-105 hover:shadow-xl dark:bg-gray-800"
					>
						<div
							class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-lg bg-blue-100 dark:bg-blue-900"
						>
							<svg
								class="h-7 w-7 text-blue-600 dark:text-blue-400"
								fill="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"
								/>
							</svg>
						</div>
						<div>
							<h4 class="mb-1 font-semibold text-gray-900 dark:text-white">Kaggle</h4>
							<p class="text-sm text-gray-600 dark:text-gray-400">kaggle.com/erayaydemir</p>
						</div>
					</a>

					<!-- Hugging Face -->
					<a
						href="https://huggingface.co/eademir"
						target="_blank"
						rel="noopener noreferrer"
						class="flex cursor-pointer items-center gap-4 rounded-xl bg-white p-6 shadow-lg transition-all hover:scale-105 hover:shadow-xl md:col-span-2 dark:bg-gray-800"
					>
						<div
							class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-lg bg-blue-100 dark:bg-blue-900"
						>
							<svg
								class="h-7 w-7 text-blue-600 dark:text-blue-400"
								fill="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm-1.5 6h3v3h-3V6zm0 4.5h3V18h-3v-7.5z"
								/>
							</svg>
						</div>
						<div>
							<h4 class="mb-1 font-semibold text-gray-900 dark:text-white">Hugging Face</h4>
							<p class="text-sm text-gray-600 dark:text-gray-400">huggingface.co/eademir</p>
						</div>
					</a>
				</div>

				<!-- Contact Form -->
				<!-- <div>
					<form onsubmit={handleSubmit} class="space-y-4">
						<div>
							<label
								for="name"
								class="mb-1 block text-sm font-medium text-gray-700 dark:text-gray-300"
							>
								Name *
							</label>
							<input
								type="text"
								id="name"
								bind:value={formData.name}
								class="w-full rounded-lg border border-gray-300 px-4 py-2 transition-all focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-800 dark:text-white {errors.name
									? 'border-red-500'
									: ''}"
								placeholder="Your name"
								disabled={isSubmitting}
							/>
							{#if errors.name}
								<p class="mt-1 text-sm text-red-600 dark:text-red-400">{errors.name}</p>
							{/if}
						</div>

						<div>
							<label
								for="email"
								class="mb-1 block text-sm font-medium text-gray-700 dark:text-gray-300"
							>
								Email *
							</label>
							<input
								type="email"
								id="email"
								bind:value={formData.email}
								class="w-full rounded-lg border border-gray-300 px-4 py-2 transition-all focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-800 dark:text-white {errors.email
									? 'border-red-500'
									: ''}"
								placeholder="your.email@example.com"
								disabled={isSubmitting}
							/>
							{#if errors.email}
								<p class="mt-1 text-sm text-red-600 dark:text-red-400">{errors.email}</p>
							{/if}
						</div>

						<div>
							<label
								for="subject"
								class="mb-1 block text-sm font-medium text-gray-700 dark:text-gray-300"
							>
								Subject *
							</label>
							<input
								type="text"
								id="subject"
								bind:value={formData.subject}
								class="w-full rounded-lg border border-gray-300 px-4 py-2 transition-all focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-800 dark:text-white {errors.subject
									? 'border-red-500'
									: ''}"
								placeholder="Project inquiry"
								disabled={isSubmitting}
							/>
							{#if errors.subject}
								<p class="mt-1 text-sm text-red-600 dark:text-red-400">{errors.subject}</p>
							{/if}
						</div>

						<div>
							<label
								for="message"
								class="mb-1 block text-sm font-medium text-gray-700 dark:text-gray-300"
							>
								Message *
							</label>
							<textarea
								id="message"
								bind:value={formData.message}
								rows="5"
								class="w-full resize-none rounded-lg border border-gray-300 px-4 py-2 transition-all focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-800 dark:text-white {errors.message
									? 'border-red-500'
									: ''}"
								placeholder="Tell me about your project..."
								disabled={isSubmitting}
							></textarea>
							{#if errors.message}
								<p class="mt-1 text-sm text-red-600 dark:text-red-400">{errors.message}</p>
							{/if}
						</div>

						<button
							type="submit"
							disabled={isSubmitting}
							class="w-full transform cursor-pointer rounded-lg bg-blue-600 px-6 py-3 font-semibold text-white shadow-lg transition-all hover:scale-105 hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
						>
							{isSubmitting ? 'Sending...' : 'Send Message'}
						</button>

						{#if submitStatus === 'success'}
							<div
								class="rounded-lg border border-green-400 bg-green-100 p-4 text-green-700 dark:border-green-700 dark:bg-green-900 dark:text-green-300"
							>
								<p class="font-semibold">Message sent successfully!</p>
								<p class="text-sm">I'll get back to you as soon as possible.</p>
							</div>
						{/if}

						{#if submitStatus === 'error'}
							<div
								class="rounded-lg border border-red-400 bg-red-100 p-4 text-red-700 dark:border-red-700 dark:bg-red-900 dark:text-red-300"
							>
								<p class="font-semibold">Something went wrong!</p>
								<p class="text-sm">Please try again later or email me directly.</p>
							</div>
						{/if}
					</form>
				</div> -->
			</div>
		</div>
	</div>
</section>
