<script lang="ts">
	let isMenuOpen = $state(false);
	let scrolled = $state(false);

	// Handle scroll effect
	if (typeof window !== 'undefined') {
		const handleScroll = () => {
			scrolled = window.scrollY > 20;
		};

		window.addEventListener('scroll', handleScroll);
	}

	function scrollToSection(sectionId: string) {
		const element = document.getElementById(sectionId);
		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
			isMenuOpen = false;
		}
	}

	const navLinks = [
		{ id: 'home', label: 'Home' },
		{ id: 'about', label: 'About' },
		{ id: 'projects', label: 'Projects' },
		{ id: 'contact', label: 'Contact' }
	];
</script>

<nav
	class="fixed top-0 z-50 w-full transition-all duration-300 {scrolled
		? 'bg-white/95 shadow-lg backdrop-blur-sm dark:bg-gray-900/95'
		: 'bg-transparent'}"
>
	<div class="container mx-auto px-6">
		<div class="flex h-16 items-center justify-between">
			<!-- Logo -->
			<button
				onclick={() => scrollToSection('home')}
				class="text-2xl font-bold {scrolled
					? 'text-gray-900 dark:text-white'
					: 'text-gray-900 dark:text-white'} transition-colors hover:text-blue-600 dark:hover:text-blue-400"
			>
				Portfolio
			</button>

			<!-- Desktop Navigation -->
			<div class="hidden items-center gap-8 md:flex">
				{#each navLinks as link}
					<button
						onclick={() => scrollToSection(link.id)}
						class="font-medium text-gray-700 transition-colors hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400"
					>
						{link.label}
					</button>
				{/each}
			</div>

			<!-- Mobile Menu Button -->
			<button
				onclick={() => (isMenuOpen = !isMenuOpen)}
				class="p-2 text-gray-700 transition-colors hover:text-blue-600 md:hidden dark:text-gray-300 dark:hover:text-blue-400"
				aria-label="Toggle menu"
			>
				{#if isMenuOpen}
					<svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M6 18L18 6M6 6l12 12"
						></path>
					</svg>
				{:else}
					<svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h16M4 18h16"
						></path>
					</svg>
				{/if}
			</button>
		</div>
	</div>

	<!-- Mobile Menu -->
	{#if isMenuOpen}
		<div
			class="border-t border-gray-200 bg-white shadow-lg md:hidden dark:border-gray-800 dark:bg-gray-900"
		>
			<div class="container mx-auto space-y-2 px-6 py-4">
				{#each navLinks as link}
					<button
						onclick={() => scrollToSection(link.id)}
						class="block w-full rounded-lg px-4 py-3 text-left font-medium text-gray-700 transition-colors hover:bg-blue-50 hover:text-blue-600 dark:text-gray-300 dark:hover:bg-gray-800 dark:hover:text-blue-400"
					>
						{link.label}
					</button>
				{/each}
			</div>
		</div>
	{/if}
</nav>

<!-- Spacer to prevent content from being hidden under fixed navbar -->
<div class="h-16"></div>
