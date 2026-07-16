# meta fixes:
- more detmermnistic work, guidacne to run command lines (insteaod of thinking) and accessing universal templates that are feeded with short run specificications (target kb, target folder, skill package)
  - instead of formulating prompts there are fixed command lines and prompt template that are used for teh different steps by all agents. 
    he q&a only created one per file per run with the different mode selectinons, paths, folder and such, that is used as instruction to run the tempaltes who have generic names e.g. skill, target kb, target lifecycle folder
- the  q&a did not work at all. the ai is thinking a lot instead of execution the process. maybe a q&a template plus a preflight for the target folder and kb are better?
  - we need to create a skill in the executiong ai (gpt browser) otherwise the apex-kb will run into repo problems as the tempaltes we are creating are not going to be accessible (target kb and  folder in another repo creates problems9
    - also codex has been thinking a lot isntead of executing scripts. i want to instgurc the ai to only execute commands, not thinking process
      - therefor we need a process that 
- ths work tree issue comes up everytime. i dont undersstnad it, it is unncessary and ai dont knwo what to do about it. 
- deliverables

# process:
- Operator: initiation of skill apex-kb
- Orhcestrator AI: Scripted Message:
	- Welcome Messsage: HelloHiHey you Nerd, wanna index something like real good? Answer these:
		- KB to get indexed ("KB-Folder"):
		- Folder to write the index i ("Index-Folder") n: 
		- Preflight Analysis: small, medium, great
		- KB type: many folders / many files / small batch
		- INtent: Short info on what needs to be done with that, what topics and questions need to get answered (this needs a lot of clear defnition as this is the possibility for the ai to drift badly)
- Operator: input
- Orhcestrator AI: Operator Input are saved as a file most likely in the index folder so that the preflight script can use its info to run the scripts and commands are run, report is created with recommendation
	- Full Instructions pre-run TEmpalte: 
		- - all options for each option (graphs yes or no, kb into raw for short list) are listed with a recommednation and teh reasoning why
		- an ai generated statement on what it understood of the intent and how it used it to create the optionsif user is new and need 
		- maybe the template has some short explanations of what will happen (phase 1 determisitc, 2 semantic, 1 determsitc, one semantic)
- Operator validation or change
- Orhcestrator AI: Changes  pre-run TEmpalte or executes scripts as commands, no thinking
- Determnistics Run:
	- finsihes noprmal run
	- then a new cscrpts (Phase1-Prompt) runs that combines the releavnat pre-run TEmpalte data (topics, intensity, grouping) and paths (both local and git paths) to create the individual insturctions for the prompt template "Phase1-Insturctions" file in the index folder ... all of that machine reabale first
	- Prompt 1: 
		- instructions: paste this as instruction into your ai and paste the report back to continue with phase 2:
			- run "Phase1-Prompt" with these instructions "Phase1-Insturctions" including their paths in the repo
- Orhcestrator AI: pastes teh above created script/command/template/message to the oeprator in the chat
- Operator: paste instructions message to what ever ai who will run it to create output 1
- Orhcestrator AI: if report validates it executes script (Phase2-Prompt) and creates file "Phase2-Insturctions" and gives back scriptes Message: "instructions: paste this as instruction into your ai and paste the report back to continue with phase 3:
- Operator feeds report to Orhcestrator
- Ai: Checks report and executes the next script withput thinking
- ... for all paheses


# questions:
- how can we make the ai not think and use its own context. just calling scripts, posting templates and executing commands?
	