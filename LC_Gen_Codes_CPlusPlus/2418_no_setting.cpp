class Solution {
    public List<String> sortPeople(List<String> names, List<Integer> heights) {
        // Create a list of tuples (name, height)
        List<Pair<String, Integer>> people = new ArrayList<>();
        
        for (int i = 0; i < names.size(); i++) {
            Pair<String, Integer> person = new Pair<>(names.get(i), heights.get(i));
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
        List<String> sortedNames = new ArrayList<>();
        for (Pair<String, Integer> person : people) {
            sortedNames.add(person.getKey());
        }
        
        return sortedNames;
    }
}