<h1>Lesson Plan</h1>

<div class="p-4">
	<div class="flex items-center space-x-4">
		<button class="px-4 py-2 bg-blue-500 text-white rounded-md">Generate New Plan</button>
		<div class="flex items-center space-x-2">
			<label for="time-length">Time Length:</label>
			<select id="time-length" class="px-4 py-2 border border-gray-300 rounded-md">
				<option value="45">45 min</option>
				<option value="90">1hr 30min</option>
				<option value="180">3hr</option>
			</select>
		</div>
		<div class="flex items-center space-x-2">
			<input type="checkbox" id="text" name="text" />
			<label for="text">Text</label>
			<input type="checkbox" id="video" name="video" />
			<label for="video">Video</label>
			<input type="checkbox" id="audio" name="audio" />
			<label for="audio">Audio</label>
			<input type="checkbox" id="mic" name="mic" />
			<label for="mic">Mic</label>
		</div>
	</div>
</div>
