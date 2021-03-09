# Coding
A collection of solved problems useful to strengthen the preparation for the coding interview at big tech companies, also known as FANG (Facebook, Amazon, Netflix and Google).

## Practice
Coding is a highly intellectual task and requires mental clarity as well as communication for a peer to grasp the logic of someone's else code. For this reason, communication is very important, even more important if coupled to a structured way of addressing the problem at hand.

Hereafter, a generic scheme to address coding problem, from the analysis to the coding.

1. **Disambiguate** - analyze the text and ask questions looking at the inputs and outputs provided. Do not stuck with the first idea that bubbles up in your mind: even if the solution is immediately clear, reason through and make sure that you are not missing anything. Remember, the evil is in the details.

2. **Identify Additional Test Cases** - looking a the inputs and outputs as well as already provided test cases, start thinking to your own. This helps disambiguate futher, for a better understanding of the problem and its intricacies.

3. **Reason About the Solution** - start thinking about the solution as steps that you might do to solve it, avoid thinking immediately in terms of coding: this might be detrimental and bias your reasoning process. Think loudly, and use concrete examples from the inputs and outputs to validate the procdural steps taht you believe might work.

4. **Describe Solution in Words** - once got a solution that works for the inputs and outputs, put it in words, this helps further clarify the contex and the successive implementation.

5. **Coding and Communicating** - following the identified steps, start the implementation. During the implementation, as much as possible, try to delegate to helper functions the subparts of the problem which are specific to some processing that it is required in the main flow: doing so, the main flow of the code will be clear and well structured (modularity will help further in testing and debugging).

6. **Debugging and Corner Cases** - once completed the implementation, make sure that it is right by debugging it visually using the inputs and outputs that have been identified. This step is fundamental to identify any corner case, as well as to discover bugs.

7. **Identify Time and Space Complexity** - as you go with coding, being mindful of the time and space complexity. Leave comments, and then reuse those comments to build the overall time and space complexity of the written code.

It is very important to leave comments in the code. This helps a lot to communicate design decisions as well as invariants according to the found solution.

## Programming Language
Like said, coding is a complex intellectual task. A Programming Language which facilitate the translation of high-level steps into working code is a sharp tool. 

Languages like Python are ideal for their human-friendliness and rich toolbox of data structures and helper functions. For this reason, the solution to the problems addressed in this project is based on Python.

## Layout
This project is a collection of already solved problems. Easy (warm ups), Medium and Hard problems are solved and commented in a way that it is easy to grasp the overall idea as well as logic.

Each section reports the problems and related solutions, as well as the references to the theory behind it.

```bash
.
├── LICENSE
├── Makefile
├── README.md
├── coding
│   ├── Makefile
│   ├── README.md
│   ├── array
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── anagram.py
│   │   ├── buy_sell_stock.py
│   │   ├── check_if_straight_line.py
│   │   ├── container_most_water.py
│   │   ├── defanging_ip_address.py
│   │   ├── duplicates.py
│   │   ├── equivalent_string_arrays.py
│   │   ├── group_anagrams.py
│   │   ├── insert_interval.py
│   │   ├── largest_triangle_area.py
│   │   ├── last_stone_weight.py
│   │   ├── matrix_block_sum.py
│   │   ├── max_nr_events.py
│   │   ├── max_subarray_product.py
│   │   ├── max_subarray_sum.py
│   │   ├── merge_intervals.py
│   │   ├── min_rotated_sorted_array.py
│   │   ├── min_time_visiting_all_points.py
│   │   ├── min_window_substring.py
│   │   ├── nonoverlapping_interval.py
│   │   ├── parentheses.py
│   │   ├── product_array_except_self.py
│   │   ├── search_rotated_search_array.py
│   │   ├── surface_area_3D_shape.py
│   │   ├── three_sum.py
│   │   ├── two_sum.py
│   │   └── valid_palindrome.py
│   ├── backtracking
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── binary_watch.py
│   │   ├── combinations.py
│   │   ├── count_matches_tournament.py
│   │   ├── count_sorted_vowel_strings.py
│   │   ├── letter_case_permutation.py
│   │   ├── maze.py
│   │   ├── pemutations.py
│   │   ├── soduku.py
│   │   └── subsets.py
│   ├── dp
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── climbing_stairs.py
│   │   ├── coin_change.py
│   │   ├── combination_sum.py
│   │   ├── fibonacci.py
│   │   ├── hand_of_straights.py
│   │   ├── house_robber.py
│   │   ├── jump_game.py
│   │   ├── lcs.py
│   │   ├── lis.py
│   │   ├── unique_paths.py
│   │   └── word_break.py
│   ├── ds-and-algo
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── add_search_words.py
│   │   ├── basic_calculator.py
│   │   ├── binarytree_maximum_path_sum.py
│   │   ├── construct_binarytree.py
│   │   ├── ealuate_rpn.py
│   │   ├── enc_dec_tiny_url.py
│   │   ├── exam_room.py
│   │   ├── expression_add_operators.py
│   │   ├── find_median_datastream.py
│   │   ├── find_median_datastream_array.py
│   │   ├── find_most_competitive_subsequence.py
│   │   ├── grumpy_bookstore_owner.py
│   │   ├── implement_heap.py
│   │   ├── implement_lru_cache.py
│   │   ├── implement_magic_dict.py
│   │   ├── implement_map.py
│   │   ├── implement_min_stack.py
│   │   ├── implement_queue_using_stacks.py
│   │   ├── implement_trie.py
│   │   ├── index_pairs_string.py
│   │   ├── invert_bst.py
│   │   ├── is_same_tree.py
│   │   ├── is_subsequence.py
│   │   ├── kth_smallest_bst.py
│   │   ├── level_order_traversal_bt.py
│   │   ├── linkedlist_cycle.py
│   │   ├── longest_word_dict.py
│   │   ├── lowest_common_ancestor_bst.py
│   │   ├── lowest_common_ancestor_bt.py
│   │   ├── match_camelcase.py
│   │   ├── match_delimiters.py
│   │   ├── max_depth_binarytree.py
│   │   ├── max_path_sum_bt.py
│   │   ├── merge_k_sorted_lists.py
│   │   ├── merge_sorted_lists.py
│   │   ├── min_nr_meeting_rooms.py
│   │   ├── moving_average_stream.py
│   │   ├── range_in_bst.py
│   │   ├── range_sum_query_mutable.py
│   │   ├── recent_counter.py
│   │   ├── remove_nth_node_from_end_list.py
│   │   ├── reorder_list.py
│   │   ├── replace_words.py
│   │   ├── search_in_bst.py
│   │   ├── serde_bt.py
│   │   ├── sort_chars_by_frequency.py
│   │   ├── sort_stack_with_stack.py
│   │   ├── subtree_bt.py
│   │   ├── task_scheduler.py
│   │   ├── top_k_frequent_elems.py
│   │   ├── validate_bst.py
│   │   └── wrap_text_in_rectangle.py
│   ├── graph
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── all_paths_from_source_to_target.py
│   │   ├── binary_number_to_integer.py
│   │   ├── clone_graph.py
│   │   ├── connected_components.py
│   │   ├── course_schedule.py
│   │   ├── destination_city.py
│   │   ├── is_a_tree.py
│   │   ├── longest_consecutive_sequence.py
│   │   ├── network_delay.py
│   │   ├── nr_of_islands.py
│   │   ├── nr_of_islands_matrix.py
│   │   └── pacific_atlantic_water_flow.py
│   └── recursion
│       ├── Makefile
│       ├── README.md
│       ├── add_digits.py
│       ├── construct_rectangle.py
│       ├── max_consecutive_ones_3.py
│       ├── power_of_four.py
│       ├── power_of_three.py
│       ├── rectangle_overlap.py
│       ├── reverse_linkedlist.py
│       ├── student_attendance_record_1.py
│       ├── subsets.py
│       ├── subsets_2.py
│       └── symmetric_tree.py
├── systems
│   └── README.md
├── theory
│   ├── README.md
│   ├── asymptotic-notation.md
│   ├── back-of-the-envelope-calculations.md
│   ├── backtracking.md
│   ├── combinatorics.md
│   ├── complexity-analysis.md
│   ├── dynamic-programming.md
│   ├── graph.md
│   ├── imgages
│   │   └── backtracking
│   │       ├── maze-gametree.png
│   │       └── maze.png
│   ├── np-completeness-hardness.md
│   ├── subarray-subsequence-substring-subset.md
│   ├── systems-design.md
│   └── traversals.md
└── transversals
    ├── Behavioral.md
    ├── Leadership.md
    ├── Management.md
    ├── README.md
    ├── gca.md
    └── project-management.md

12 directories, 160 files
```

# References

- [LeetCode](https://leetcode.com/explore/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/?ref=shm)
- [Daily Coding Problem](https://github.com/Jedshady/daily-coding-problem)
