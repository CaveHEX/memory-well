from memory import memory_t

def main():
    print("Memory Well")
    mem = memory_t()
    mem.set_memory("I did a thing")



if __name__ == "__main__":
    main()


# team = Team(students=[student1, student2])
 
# Serialization
# json_data = json.dumps(team, default=lambda o: o.__dict__, indent=4)
# print(json_data)
 
# Deserialization
# decoded_team = Team(**json.loads(json_data))
# print(decoded_team)
