# Unity - Godot API Quick Reference

| Unity  C# | GDScript | Note |
|----------|------|
| Random.Range | rand_range() |  in Godot call randomize() once in your program to se the random seed |
| Random.insideUnitCircle | ? | Random Vector2 of unit length |
| Random.insideUnitSphere |``` static func random_point_in_unit_sphere() -> Vector3:
	var theta = rand_range(0, 2 * PI)
	var phi = rand_range(0, PI)
	var r = pow(rand_range(0, 1), 1.0/3.0)  # Cube root for uniform distribution

	var x = r * sin(phi) * cos(theta)
	var y = r * sin(phi) * sin(theta)
	var z = r * cos(phi)
	return Vector3(x, y, z) ```` | Random Vector3 of unit length in Unity, in Godot will not be of unit length, but can be normalized |
| transform.position | global_transform.origin | World space position |
| transform.rotation | global_transform.basis | In Unity, a quaternion, in Godot rotation is a 3x3 matrix containing scale and rotation. It can be extracted into a quaternion for quaternion operations with ```get_rotation_quat()``` |
| transform.localScale | transform.basis.get_scale() transform.basis.scaled |  Relative to the parent |
| transform.localPosition | transform.origin | transform is the local transform |
| transform.localRotation | transform.basis |
| transform.Translate | translate | |
| transform.Rotate | rotate | |
| transform.RotateAround | ? | Takes point, axis and angle. This and the subsequent call loose precision after a while |
| transform.RotateAroundLocal | ? |Takes point, axis and angle |
| transform.SetParent | add_child |  |
| transform.up | transform.basis.y | Local up  |
| transform.right | transform.basis.x | Local right |
| transform.forward | transform.basis.z |Local forward |
| transform.TransformPoint | transform.xform | Scales, rotates and transforms a point by a transform. Local to world space |
| transform.InverseTransformPoint | transform.xform_inv | Scales, rotates and transforms a point by a transform. World to local space |
| transform.TransformDirection | transform.basis.xform | Not affected by scale or position. Godot version is affected by scale |
| transform.LookAt | look_at | Rotates so that transform.forward (Unity) or global_transform.basis.z points at a position | 
| transform.ChildCount() | get_child_count() | returns the number of children transforms parented to this transform |
| transform.GetChild(0) | get_child(0) | returns child 0 |
| gameObject.SetActive | set_process | Disables and enables a gameobject and any components attached to it will not have the Update method called |
| gameObject.name | .name | Name in the hierarchy |
| gameObject.Tag | Don't think these exist in Godot |Set up the strings in the Unity editor. Can use with FindGameObjectWithTag |
| gameObject.layer | get_collision_layer_bit(), set_collision_layer_bit() | A number. Set up different layers for different groups of objects like environment, different enemy types. Use with layer masks. Used for raycasting and rendering |
| gameObject.GetComponent<> | get_node("NodeName") | To return a component attached to a gameobject. Uses generics. Returns null if there is no component attached |
| gameObject.AddComponent<> | add_child() | Retuns the new component |
| gameObject.GetComponentInChildren | Recursive search |
| GameObject.FindGameObjectWithTag<> | Returns the first matching object |
| GameObject.FindGameObjectsWithTag<> | Returns a typed array of objects |
| GameObject.CreatePrimitive | Creates cubes, spheres, cylinders etc |
| GameObject.Destroy | Pass in the gameobject or component you want to distroy |
| GameObject.FindObjectOfType |  Searches the memory space for an instance of a class |
| Vector3.Dot | Multiplies 2 vectors returns a scalar. In front/behind or calculating angle between 2 vectors |
| Vector3.Lerp | Interpolates between 2 vectors using t |
| Vector3.Cross | Returns a vector that is mutully perpindicular to the 2 parameters |
| Vector3.Normalize | Makes the vector of length 1 |
| Vector3.Up | The world up vector |
| Vector3.Right | |
| Vector3.Forward | |
| Vector3.Zero | The vector (0,0,0)  |
| Vector3.One | The vector (1,1,1) |
| Vector3.Distance | Distance between 2 position vectors |
| Vector3.Angle | Angle between 2 vectors |
| x, y, z, | Note vectors are value types! (Structs) |
| vector3.normalized | |
| Quaternion.AngleAxis | This is how to make a quaternion! Angle is in degrees |
| Quaternion.Slerp |  Interpolates between 2 quaternions |
| Quaternion.Identity | No rotation |
| Quaternion.Euler | Make a quetarnion from euler angles |
| Quaternion.Inverse | Quaternion in the opposite direction |
| Quaternion.LookRotation | Makes a quaternion from a vector |
| Quaternion * by a Vector3 | Rotates the vector by the quaternion |
| Quaternion * by a Quaternion | Combines 2 quaternion rotations |
| x, y, z, w | Components of the quaternion |
| Input.GetAxis("Vertical") | returns a value between 0 and 1. Used to move things in response to user input |
| Input.GetKey(KeyCode.Escape) | Check if a key is currently being pressed |
| Input.GetButtonDown("Fire1") | Check if a button is pressed this frame |
| OnDrawGizmos | Called by the Unity editor. Allows the game component to draw gizmos to the scene view |
| Gizmos.color | Sets the color of the subsequently drawn gizmos |
| Gizmos.DrawSphere | |
| Gizmos.DrawWireSphere | |
| Gizmos.DrawCube | |
| Gizmos.DrawLine | |
| Gizmos.DrawRay | |