General questions:

- What tools are needed to do this line of work? I'm willing to learn.
- Is it viable for non-US person like me to work on adjacent problems like these as a job, if so what do you recommand me to do? Things to learn, communities to join, type of projects to work on/write about.


# [How understanding valence could help make future AIs safer](https://opentheory.net/2015/09/fai_and_valence/)

This article is like thunder through my ears, Michael's ideas arguments speaks to me intuitively, they matched many of my own musings yet better articulated than I could.

I agree with almost all points raised in this article, except the point about wire-heading (I guess I'm more skeptical/confused about the concept of wire-heading itself than Michaels agrument about it).

The first point of value-loading resonates with me the most. How are we going to know what should the agi do if we don't about the subjects they're going to work upon, and are there any universal principles? It's like doing optimization theory research without looking into the many data distributions empirically. 

Working on valence helps AGI safety yet is orthogonal to speeding up AGI is also a very good point.

The article is very thought-provoking to me, the following is the loosely organized thoughts I have while reading it.

## My deep confusions about wire-heading:

The idea that the objective and valence of an agent are different things is such a subtle point and Michael agrued much better than me in my older mind. But thinking of it there's many unknowns about it (to me at least, it is likely that I'm just deeply ignorant about agents and utilities etc and what's written below doesn't make sense).

(I'm about to study Sutton's RL after finishing the batch of book I'm reading, and I will update on any misunderstandings after that).

- External, loaded utility function in the RL sense vs the *true* objective of an agent in the formal sense are different concepts and should be better distinguished.
	If subjective valence affects the agent's behavior at all, it should be included as part of the formal objective of the agent. The fact that they're discussed as separate here probably indicates Michael meant to talk about objective in the RL sense, which is loaded externally. 
	(If that's not the case than I must have been confused about what utility and valence mean here.)

- Thinking about wire-heading reveals that I don't understand the relationship between subjective valence, utility and behavior.

- How does valence and behavior interact with each other? What do we meand that we want sth (is it because that's described by utility and our model is trained/guided by it, or because we feel good so we want it)?
	Do we (and agents with subjective experience in general) want to move to a state with higher valence fundamentally, or it's a some how learned policy? 
	I think it's the former and that might have sth to do with what valence is? 
	If it's the latter then it's really bizarre why that's picked up by evolution, and it's also bad news that this might not be universal.

- Which comes first?
	we have objectives as agents and we find activities that matches the objective as pleasent via self-modeling; 
	or first exist fundamental principles of valence and objectives evolved to fit criteria of self-replication toward positive valence in agents; 
	or they're separate things, have more complex relationship with each other? 
	I think valence comes first, and evolution picked up on it (related to last q); but also if valence is low-complexity concept (so many different agent designs represent similar valence level etc), there's likely exist ways to morph it in the design space to match a existing objective. Not sure whether it make sense or not but it's very confusing.

- I'm not convinced by the significance of the wire-heading concept
	I don't think I understand the concept deeply (I've read Superintelligence and find it confusing back then). But if it literally means what mice did in the OG wire-heading experiment, whatever positive and negative experience we persue can be seen as a less extreme version of wire-heading! Wire-heading (of this definition) isn't a binary concept. And suddenly most of the elements in the set of wire-heading behavior felt much less deadly! Like sex, sleep, friendship, learning sth new...

- I think treating objectives as some external oracle has its blind-spots (this is what I believe the wire-heading argument stands).
	Following the previous point. For us human minds, the part of brain/mind that evaluates the the state we're in are also part of the brain. The question isn't whether we can directly manipulate the *utility* but how dexterous we are when interfacing with it and how different utilities are coherent or not. The same is true for AIs. Currently human utilities are greatly under-actuated, but if those utility evaluators can work with so many complex states, how likely is it that they are also agents themselves with their own feedback cycle of actions and their subsequent effects?
	And even though it looks clean and clear to distinguish input of environment state and reward signal in math formalism, I always find it fishy. Seems like what we choose as evaluation for reward (by parts of ourselves) and feed the evaluation to other parts of the agent/mind/whatever is important here.
	
## My thoughts about valence and possible research directions

I haven't read QRI's research on valence yet, and I want to write down what I thought about it beforehand:

- I used to think of happiness (similar to valence mentioned here) as in a state that one doesn't want to leave in a sense that it generates coherent predictions from all of its parts. 
	To achieve this in a dynamic world of ours, it needs to be robust towards change while adapt to them, so it prefers states that's not boring/static (too brittle) yet is predictable/compressable (in the format of the specific mind). 
	And since it's active, it has to be spatially and temporally constrained to varify its predictions/manipulations of the world (I also suspect static data have feelings). 
	I find it loosely analogous to the free-energy principle.
	I used to think of it from the utilitarian perspective: that agents want this will survive. But now I suspect there's something more fundamental about it if valence comes first. 
	I'm not sure if this make sense or not, but it's really intriguing to me that the two directions match in...this world (adaptive states feel good, and good-feeling states help survive). 

- And if I were to work on things adjacent to what Michael has written, I might try to figure out how objectives and levels of valence effect parts of an agent. 
	If valence is about the distribution of predictions given by different parts (sub-agents), I think the questions is how seriously should we view this claim? As a hand-wavy analogy that part of brains want different things, or as rigorous description that agents can be decomposed to smaller agents with their own utility and models the effects of their actions on the environment (mostly neighbor sub-agents)? 
	I tend to think it's the latter. And since this is a fairly strong assumption, it's going to be very useful to figure out what kinds of agents have such internal structures and how to find them, evaluate their goals, see how different levels of hierarchy relate to each other, etc. If we can recursively break down an agent to its self-similar parts for a wide range of different agents I suspect we can do much in divide-and-conquer sense.

