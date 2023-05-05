<h1>Installing Necessary Libraries</h1>
<p>
    The required Libraries for the Taxi.py file to work are:

</p>
<ol>
    <li>Numpy Library</li>
    <li>Gym Library</li>
</ol>

<p>Use pip to install these Libraries. open the cmd and type <b>pip install numpy</b> to install numpy and <b>
        pip install gym
    </b> to install gym Library which contains the Taxi Environmnet</p>

<h2>What's a Taxi Envirnment</h2>

<p>
    <ol>
        <li>Taxi is one of many environments available on OpenAI Gym.
            These environments are used to develop and benchmark reinforcement learning algorithms.</li>
        <li>The goal of Taxi is to pick-up passengers and drop them off at the destination in the least amount of moves.
            In this tutorial, you'll start with a taxi agent that takes actions randomly</li>
        <li>
            We also need to train the agent to be a better taxi driver using reinforcement learning
        </li>
    </ol>

</p>

<h2>
    An introduction to Reinforcement Learning:
</h2>
<p>Think about how you might teach a dog a new trick, like telling it to sit:</p>
<ul>
    <li>If it performs the trick correctly (it sits), you'll reward it with a treat (positive feedback) ✔️</li>
    <li>If it doesn't sit correctly, it doesn't get a treat (negative feedback) ❌</li>
</ul>
<p>By continuing to do things that lead to positive outcomes, the dog will learn to sit when it hears the command in
    order to get its treat. Reinforcement learning is a subdomain of machine learning which involves training an 'agent'
    (the dog) to learn the correct sequences of actions to take (sitting) on its environment (in response to the command
    'sit') in order to maximise its reward (getting a treat)</p>

<h2>Random Agent</h2>
<p>We'll start by implementing an agent that doesn't learn at all.
    Instead, it will sample actions at random. This will be our baseline.</p>
<p>The first step is to give our agent an initial state of its environment. A state is how our agent will observe its
    environment. In Taxi, a state defines the current positions of the
    taxi, passenger, and pick-up and drop-off locations.</p>
<p><b>Note: </b>Yellow = taxi, Blue letter = pickup location, Purple letter = drop-off destination</p>

<p>Next, we'll run a for-loop to cycle through the game. At each iteration, our agent will:</p>
<ol>
    <li>Make a random action from the action space (0 - south, 1 - north, 2 - east, 3 - west, 4 - pick-up, 5 - drop-off)
    </li>
    <li>Receive the new state</li>
</ol>
<h2>📖 Q-Learning Agent</h2>
<p>Q-learning is a reinforcement learning algorithm that seeks to find the
    best possible next action given its current state, in order to maximise
    the reward it receives (the 'Q' in Q-learning stands for quality - i.e. how valuable an action is).</p>
<h2>Taxi Reward Sysytm</h2>
<p>The Agent receive +20 points for a successful drop-off, and lose 1 point for every timestep it takes.
    There is also a 10 point penalty for illegal pick-up and drop-off actions.</p>

<h2>Exploration</h2>
<p>Our agent currently has no way of knowing which action will lead it closest to the blue R. This is where
    trial-and-error comes in
    we'll have our agent take random actions, and observe what rewards it gets (i.e. our agent will explore).</p>
<p>Over many iterations, our agent will have observed that certain sequences of actions will be more rewarding than
    others.
    Along the way, our agent will need to keep track of which actions led to what rewards.</p>
<h2>Introducing… Q-tables</h2>
<p>A Q-table is simply a look-up table storing values representing the maximum expected
    future rewards our agent can expect for a certain action in a certain state (known as Q-values).
    It will tell our agent that when it encounters a certain state, some actions are more likely than
    others to lead to higher rewards. It becomes a 'cheatsheet' telling our agent what the best action to take is.</p>
<ol>
    <li>Each row corresponds to a unique state in the 'Taxi' environment</li>
    <li>Each column corresponds to an action our agent can take</li>
    <li>Each cell corresponds to the Q-value for that state-action pair
        a higher Q-value means a higher maximum reward our agent can expect to get if it takes that action in that
        state.</li>
</ol>

<p>As our agent explores,
    it will update the Q-table with the Q-values it finds. To calculate our Q-values, we'll introduce the Q-learning
    algorithm.</p>

<h2>
    Q-Learning Algorithm
</h2>
<p>The Q learning Algorith formula is given Below</p>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686" alt="">

<p>The Q-learning algorithm will help our agent update the current Q-value (Q(St,At)) with its observations after taking
    an action. I.e.
    increase Q if it encountered a positive reward, or decrease Q if it encountered a negative one.</p>
<p>
    Note that in Taxi, our agent doesn't receive a positive reward until it successfully drops off a passenger (+20
    points). Hence even if our agent is heading in the correct direction,
    there will be a delay in the positive reward it should receive
</p>

<p>The 'a' term refers to all the possible actions
    available for that state. The equation also contains two hyperparameters which we can specify:</p>
<ol>
    <li>Learning rate (α): how easily the agent should accept new information over previously learnt information</li>
    <li>Discount factor (γ): how much the agent should take into consideration
        the rewards it could receive in the future versus its immediate reward</li>
</ol>

<h2>Exploration vs Exploitaion</h2>
<p>We can let our agent explore to update our Q-table using the Q-learning algorithm. As our agent learns more about the
    environment,
    we can let it use this knowledge to take more optimal actions and converge faster known as exploitation</p>
<p>
    During exploitation, our agent will look at its Q-table and select the action with
    the highest Q-value (instead of a random action). Over time,
    our agent will need to explore less, and start exploiting what it knows instead.
</p>
<h2>Bringing it all together</h2>
<p>We're done with all the building blocks needed for our reinforcement learning agent.
    The process for training our agent will look like:</p>
<ol>
    <li>Initialising our Q-table with 0's for all Q-values</li>
    <li>Let our agent play Taxi over a large number of games</li>
    <li>Continuously update the Q-table using the Q-learning algorithm and an
        exploration-exploitation strategy</li>
</ol>
