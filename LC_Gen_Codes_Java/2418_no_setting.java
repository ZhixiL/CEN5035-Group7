class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // Create a list of tuples (name, height)
        List<Pair<String, Integer>> people = new ArrayList<>();
        for (int i = 0; i < names.length; i++) {
            Pair<String, Integer> person = new Pair<>(names[i], heights[i]);
            people.add(person);
        }
        
        // Sort the list of tuples by height in descending order
        Collections.sort(people, new Comparator<Pair<String, Integer>>() {
            @Override
            public int compare(Pair<String, Integer> p1, Pair<String, Integer> p2) {
                return p2.getValue().compareTo(p1.getValue());
            }
        });
        
        // Extract the names from the sorted list of tuples
        String[] sortedNames = new String[people.size()];
        for (int i = 0; i < people.size(); i++) {
            sortedNames[i] = people.get(i).getKey();
        }
        
        return sortedNames;
    }
}