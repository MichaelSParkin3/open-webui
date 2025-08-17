<script>
	import { page } from '$app/stores';
</script>

<div class="flex flex-col h-full">
	<div class="flex border-b border-gray-200 dark:border-gray-800">
		<a href="/spanish/lesson-plan" class="px-4 py-2 text-sm font-medium {$page.url.pathname.startsWith('/spanish/lesson-plan') ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'}">Lesson Plan</a>
		<a href="/spanish/flashcards" class="px-4 py-2 text-sm font-medium {$page.url.pathname.startsWith('/spanish/flashcards') ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'}">Flashcards</a>
		<a href="/spanish/class" class="px-4 py-2 text-sm font-medium {$page.url.pathname.startsWith('/spanish/class') ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'}">Class</a>
	</div>
	<div class="flex-1 overflow-y-auto">
		<slot />
	</div>
</div>
